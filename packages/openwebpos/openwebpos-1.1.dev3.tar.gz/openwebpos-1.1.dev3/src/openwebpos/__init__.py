import os
import sys
from datetime import datetime
import importlib.util
from importlib.metadata import version

from flask import Flask, send_from_directory, redirect, url_for, render_template
from sqlalchemy.exc import OperationalError

from sqlalchemy_utils import database_exists

from openwebpos.blueprints import blueprints
from openwebpos.blueprints.user.models import User
from openwebpos.blueprints.pos.models.order import OrderType, OrderPager, \
    TransactionType
from openwebpos.extensions import db, login_manager, toolbar
from openwebpos.utils import create_folder, create_file, gen_urlsafe_token


def insert_default_data() -> None:
    """
    Insert default data into the database.
    """
    # Insert default user
    User.insert_user()
    OrderType.insert_order_types()
    OrderPager.insert_order_pagers()
    TransactionType.insert_transaction_types()


def open_web_pos(instance_dir=None):
    """
    Create the Flask app instance.

    Args:
        instance_dir (str): Path to the instance folder.

    Returns:
        Flask: Flask app instance.
    """
    template_dir = 'ui/templates'
    static_dir = 'ui/static'
    base_path = os.path.abspath(os.path.dirname(__file__))

    if instance_dir is None:
        instance_dir = os.path.join(os.getcwd(), 'instance')

    if os.path.isdir(instance_dir):
        if not os.listdir(instance_dir):
            create_file(file_path=os.getcwd(), file_name='instance/__init__.py')

    create_folder(folder_path=os.getcwd(), folder_name='instance')
    create_folder(folder_path=os.getcwd(), folder_name='uploads')
    create_file(file_path=os.getcwd(), file_name='.env',
                file_content=f'SECRET_KEY="{gen_urlsafe_token(64)}"')

    app = Flask(__name__, template_folder=template_dir,
                static_folder=static_dir, instance_relative_config=True,
                instance_path=instance_dir)

    # Default settings
    app.config.from_pyfile(os.path.join(base_path, 'config/settings.py'))
    # Instance settings (overrides default settings)
    app.config.from_pyfile(os.path.join('settings.py'), silent=True)

    @app.context_processor
    def utility_processor():
        def get_package_version(package: str) -> str:
            """
            Get installed package version
            Args:
                package: String: Name of package
            Return:
                Version
            """
            try:
                if package in sys.modules:
                    # Module is already loaded
                    return version(package)
                else:
                    # Module is not loaded
                    spec = importlib.util.find_spec(package)
                    if spec is None:
                        return 'Not Installed'
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return version(package)
            except ModuleNotFoundError:
                return f'{package} not installed'

        def get_company_name() -> str:
            """
            Get company name from settings.
            """
            from openwebpos.blueprints.admin.models import Company
            company = Company.query.first()
            return company.name if company else 'OpenWebPOS'

        return dict(get_package_version=get_package_version,
                    get_company_name=get_company_name)

    @app.template_filter()
    def format_datetime(value, schema='full'):
        """
        Format datetime object to a string.

        schema: full, short, time, date

        Args:
            value (datetime): Datetime object.
            schema (str): Schema to format the datetime. Default: 'full'
                        default: YYYY-MM-DD HH:MM:SS
                        date: YYYY-MM-DD
                        short_date: MM/DD/YYYY
                        time: HH:MM:SS

        Returns:
            str: Formatted datetime.

        Examples:
            {{ datetime | format_datetime }}
            {{ datetime | format_datetime('short') }}

        """
        if value is None:
            return ''

        if schema == 'full':
            return value.strftime('%Y-%m-%d %H:%M:%S')
        elif schema == 'date':
            return value.strftime('%Y-%m-%d')
        elif schema == 'short':
            return value.strftime('%m/%d/%y')
        elif schema == 'time':
            return value.strftime('%H:%M:%S')

    # Register routes
    routes(app)

    # Load extensions
    extensions(app)

    return app


def extensions(app):
    """
    Register Extensions.

    Args:
        app (Flask): Flask app instance.
    """
    # from openwebpos.extensions import db, login_manager
    db.init_app(app)
    login_manager.init_app(app)
    toolbar.init_app(app)

    @login_manager.user_loader
    def load_user(uid):
        """
        Load user from the database.

        Args:
            uid (int): User ID.

        Returns:
            User: User object.

        TODO: Add exception errors to log file.
        """
        try:
            return User.query.get(uid)
        except OperationalError:
            print('Database not configured')

    login_manager.login_view = 'user.login'

    return app


def routes(app):
    """
    Register Routes.

    Args:
        app (Flask): Flask app instance.
    """
    from openwebpos.forms import DatabaseConfigForm

    @app.route('/')
    def index():
        if database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
            return redirect(url_for('pos.index'))
        return redirect(url_for('database_config'))

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    @app.get('/database_config')
    def database_config():
        form = DatabaseConfigForm()
        return render_template('database_config.html', title='Database Config',
                               form=form)

    @app.post('/database_config')
    def database_config_post():
        form = DatabaseConfigForm()
        if form.validate_on_submit():
            if form.dialect.data == 'sqlite':
                create_file(file_path=os.getcwd(),
                            file_name='instance/settings.py',
                            file_mode='w',
                            file_content="DB_DIALECT = 'sqlite'\n")
                db.create_all()
                insert_default_data()
                return redirect(url_for('user.login'))
            else:
                dialect = "DB_DIALECT = " + "'" + form.dialect.data + "'" + "\n"
                create_file(file_path=os.getcwd(),
                            file_name='instance/settings.py',
                            file_mode='w',
                            file_content=dialect)
                try:
                    db.create_all()
                except ConnectionError:
                    pass
                lines = [
                    "DB_DIALECT=" + "'" + form.dialect.data + "'",
                    "DB_USER=" + "'" + form.username.data + "'",
                    "DB_PASS=" + "'" + form.password.data + "'",
                    "DB_HOST=" + "'" + form.host.data + "'",
                    "DB_PORT=" + "'" + form.port.data + "'",
                    "DB_NAME=" + "'" + form.database.data + "'"
                ]
                with open(os.path.join(os.getcwd(), '.env'), 'w') as f:
                    f.write('\n'.join(lines))
                return redirect(url_for('user.login'))
        return redirect(url_for('pos.index'))

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
