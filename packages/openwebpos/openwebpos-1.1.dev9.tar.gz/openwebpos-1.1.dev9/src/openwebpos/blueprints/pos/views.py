from escpos import *

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

from openwebpos.blueprints.user.decorators import staff_required
from openwebpos.blueprints.pos.models.order import OrderType, Order, \
    OrderPager, OrderItem, TransactionType, Transaction, OrderItemOption
from openwebpos.blueprints.pos.models.menu import Menu, Item, Recipe
from openwebpos.blueprints.admin.models import Company, CompanyLocation, \
    CompanyPrinter

from .forms import AddItemToOrderForm, TransactionForm

pos = Blueprint('pos', __name__, template_folder='templates', url_prefix='/pos')


@pos.before_request
@login_required
@staff_required
def before_request():
    """
    Protects all the pos endpoints.
    """
    pass


def kitchen_printer(name="Default"):
    """
    Returns a kitchen printer instance.
    """
    # _kitchen_printer = Printer.query.filter_by(location='Kitchen').first()
    _kitchen_printer = CompanyPrinter.query.filter_by(name=name).first()
    if _kitchen_printer:
        return printer.Network(_kitchen_printer.ip, _kitchen_printer.port)
    return None


def kitchen_receipt(order_number):
    price = 0
    quantity = 0
    item_option = ''
    receipt_subtotal = 0
    purchases = []
    receipt_width = 24

    _order = Order.query.filter_by(orderNumber=order_number).first_or_404()
    order_items = OrderItem.query.filter_by(orderID=_order.id).all()
    order_item_options = OrderItemOption.query.filter_by(
        orderID=_order.id).all()

    pager = _order.order_pager.name

    receipt_content = [
        'Kitchen'.center(receipt_width),
    ]

    for order_item in order_items:

        item_options = []

        for options in order_item_options:
            if options.orderItemID == order_item.id:
                item_option = options.type + '  ' + options.ingredient.name
                item_options.append(item_option)

        name = order_item.item.menu.name + ' - ' + order_item.item.name
        item = name
        quantity = order_item.quantity
        price = order_item.item.price
        receipt_subtotal += price * quantity
        purchases.append((item, quantity, item_options))

    for item, quantity, item_options in purchases:
        item_name = f'{item}'.ljust(receipt_width - 10, '-')
        purchase_line = f'{quantity}'.ljust(
            receipt_width - (len(item_name) + 5), '-')
        purchase_line += item_name
        if item_options:
            for option in item_options:
                purchase_line += f'\n     {option}'
        receipt_content.append(purchase_line)
        receipt_content.append(''.ljust(receipt_width - 4))

    receipt_content.append(pager.center(receipt_width))

    receipt_printer = kitchen_printer()
    receipt_printer.set(height=3, width=3, font='b', text_type='B')
    receipt_printer.text("\n".join(receipt_content))
    receipt_printer.cut()


def customer_receipt(order_number):
    _company = Company.query.first()
    _company_location = CompanyLocation.query.first()
    _order_date = Order.query.filter_by(
        orderNumber=order_number).first_or_404().created_on

    price = 0
    quantity = 0
    receipt_subtotal = 0
    purchases = []
    receipt_width = 48

    # shop_name = _store.name.title().center(receipt_width)
    shop_name = _company.name.title().center(receipt_width)
    shop_address = f'{_company_location.address}\n{_company_location.city}, {_company_location.state} {_company_location.zipcode}'
    shop_address = shop_address.splitlines()
    shop_phone = f'{_company_location.phone}'
    if shop_phone == 'None':
        shop_phone = ''
    order_date = f'{_order_date.strftime("%m/%d/%Y %I:%M %p")}'
    receipt_message = 'Thank you for your business!\nPlease come again!'
    receipt_message = receipt_message.splitlines()
    # receipt_subtotal += price * quantity
    tax_percentage = 8.25
    tax_percentage = "{:.0%}".format(tax_percentage)
    # receipt_total = 0
    receipt_content = [
        shop_name,
        shop_address[0].center(receipt_width),
        shop_address[1].center(receipt_width),
        shop_phone.center(receipt_width),
        '\n',
    ]

    order_id = Order.query.filter_by(orderNumber=order_number).first_or_404().id
    order_items = OrderItem.query.filter_by(orderID=order_id).all()
    for order_item in order_items:
        name = order_item.item.menu.name + ' - ' + order_item.item.name
        quantity = order_item.quantity
        price = order_item.item.price
        receipt_subtotal += price * quantity
        purchases.append((name, quantity, price), )

    for name, quantity, price in purchases:
        line_subtotal = '$' + str(round(quantity * price, 2))
        purchase_line = f'{name}'.ljust(receipt_width - len(line_subtotal), '.')
        purchase_line += line_subtotal
        if type(quantity) is int and quantity >= 1:
            purchase_line += f'     {quantity} @ {price} /ea'
        receipt_content.append(purchase_line)

    receipt_subtotal = str(round(receipt_subtotal, 2))
    receipt_tax = str(round(float(receipt_subtotal) * 0.0825, 2))
    receipt_total = str(round(float(receipt_subtotal) + float(receipt_tax), 2))

    receipt_content.append('\n')
    receipt_content.append('    Subtotal: '.rjust(
        receipt_width - len(receipt_subtotal) - 1) + '$' + receipt_subtotal)
    receipt_content.append('    Tax: '.rjust(
        receipt_width - len(receipt_tax) - 1) + '$' + receipt_tax)
    receipt_content.append('    Total: '.rjust(
        receipt_width - len(receipt_total) - 1) + '$' + receipt_total)

    receipt_content.append('\n'.ljust(receipt_width, '*'))
    receipt_content.append(receipt_message[0].center(receipt_width))
    receipt_content.append(receipt_message[1].center(receipt_width))
    receipt_content.append(f'{order_number}'.center(receipt_width))
    receipt_content.append(f'{order_date}'.center(receipt_width))

    receipt_printer = kitchen_printer()
    receipt_printer.set(height=1, width=1)
    receipt_printer.text("\n".join(receipt_content))
    receipt_printer.cut()


@pos.get('/print/<string:style>/<string:order_number>')
def print_receipt(style, order_number):
    if style == 'kitchen':
        kitchen_receipt(order_number)
    elif style == 'customer':
        customer_receipt(order_number)
    return index()


@pos.get('/')
def index():
    _orders = Order.query.filter_by(active=True).all()
    if _orders:
        return order_list()
    return order_type()


@pos.get('/order/<string:order_number>')
def order(order_number):
    _order = Order.get_by_order_number(order_number)
    _menus = Menu.list_active()
    _menu_items = Item.query.filter_by(active=True).all()
    _menu_recipes = Recipe.query.all()
    _order_items = OrderItem.get_order_items(_order.id)
    _transaction_types = TransactionType.list_active()
    _item_options = OrderItemOption.query.filter_by(active=True,
                                                    orderID=_order.id).all()
    _order_item_options = OrderItemOption.query.filter_by(
        orderID=_order.id).all()
    form = TransactionForm()
    add_item_form = AddItemToOrderForm()
    return render_template('pos/order.html', order=_order,
                           title=_order.orderNumber, menus=_menus,
                           order_items=_order_items, menu_items=_menu_items,
                           transaction_types=_transaction_types, form=form,
                           add_item_form=add_item_form,
                           menu_recipes=_menu_recipes,
                           order_item_options=_order_item_options)


@pos.get(
    '/order/<string:order_number>/<int:order_item_id>/<int:ingredient_id>/<string:order_type>/add')
def add_order_item_option(order_number, order_item_id, ingredient_id,
                          order_type):
    _order = Order.get_by_order_number(order_number)
    _order_item_option = OrderItemOption(orderID=_order.id,
                                         orderItemID=order_item_id,
                                         ingredientID=ingredient_id,
                                         type=order_type)
    _order_item_option.save()
    return redirect(url_for('pos.order', order_number=order_number))


@pos.get('/order/pay/<string:order_number>')
def pay_order(order_number):
    _order = Order.get_by_order_number(order_number)
    _orderID = _order.id
    _menus = Menu.query.filter_by(active=True).all()
    _order_items = OrderItem.query.filter_by(orderID=_orderID).all()
    _transaction_types = TransactionType.list_active()
    _transaction = Transaction.query.filter_by(orderID=_orderID).first()
    _transactions = Transaction.query.filter_by(orderID=_orderID).all()
    form = TransactionForm()
    add_item_form = AddItemToOrderForm()
    return render_template('pos/pay_order.html', order=_order,
                           title=_order.orderNumber, menus=_menus,
                           order_items=_order_items, transaction=_transaction,
                           transaction_types=_transaction_types, form=form,
                           transactions=_transactions,
                           add_item_form=add_item_form)


@pos.post('/transaction/<string:order_number>/<string:transaction_type>/')
def transaction(order_number, transaction_type):
    _order = Order.get_by_order_number(order_number)
    _transaction_type = TransactionType.query.filter_by(
        name=transaction_type).first_or_404()
    form = TransactionForm()
    if form.validate_on_submit():
        Transaction.add_transaction(_order.id, _transaction_type.id,
                                    form.amount.data, _order.orderDueTotal)
        _order.update_order_due_total()
        _order.set_order_status()
        # return redirect(url_for('pos.kitchen', order_number=order_number))
        kitchen_receipt(order_number)
    return redirect(url_for('pos.pay_order', order_number=order_number))


@pos.post('/order/<string:order_number>/<int:menu_id>/<int:item_id>')
def test_post(order_number, menu_id, item_id):
    form = AddItemToOrderForm()
    _menu = Menu.query.filter_by(id=menu_id).first_or_404().name
    _item = Item.query.filter_by(id=item_id).first_or_404().name
    _orderID = Order.query.filter_by(orderNumber=order_number).first_or_404().id
    _itemID = Item.query.filter_by(id=item_id).first_or_404().id
    _itemPrice = Item.query.filter_by(id=item_id).first_or_404().price
    if form.validate_on_submit():
        OrderItem.add_to_order(_orderID, _itemID, form.quantity.data,
                               subtotal=_itemPrice * int(form.quantity.data))
        _order = Order.query.filter_by(orderNumber=order_number).first_or_404()
        _order.update_order_total()
    return redirect(url_for('pos.order', order_number=order_number))


@pos.get('/order/<int:order_item_id>/delete')
def remove_item(order_item_id):
    _order_item = OrderItem.query.filter_by(id=order_item_id).first_or_404()
    _order = Order.query.filter_by(id=_order_item.orderID).first_or_404()
    _order_item_option = OrderItemOption.query.filter_by(
        orderItemID=order_item_id).all()
    for option in _order_item_option:
        option.delete()
    _order_item.delete()
    _order.update_order_total()
    return redirect(url_for('pos.order', order_number=_order.orderNumber))


@pos.get('/order/<string:order_number>/delete/<int:order_item_id>')
def delete_order_item(order_number, order_item_id):
    _order_item = OrderItem.query.filter_by(id=order_item_id).first_or_404()
    _order = Order.query.filter_by(orderNumber=order_number).first_or_404()
    _order_item.delete()
    _order.update_order_total()
    return redirect(url_for('pos.order', order_number=order_number))


@pos.get('/order-type')
def order_type():
    _order_types = OrderType.query.filter_by(active=True).all()
    _order_pagers = OrderPager.query.filter_by(active=True, hidden=False).all()
    _has_order_pagers = OrderPager.has_pagers()
    return render_template('pos/order_type.html', title='Order Types',
                           order_types=_order_types, order_pagers=_order_pagers,
                           has_order_pagers=_has_order_pagers)


@pos.get('/order-list')
def order_list():
    _orders = Order.query.filter_by(active=True).all()
    _order_items = OrderItem.query.all()
    if _orders is None:
        return order_type()
    return render_template('pos/order_list.html', title='Order List',
                           orders=_orders, order_items=_order_items)


@pos.get('/finish-order/<int:order_id>')
def finish_order(order_id):
    _order = Order.query.filter_by(id=order_id).first_or_404()
    _order.active = False
    _order.save()
    _order_pager = OrderPager.query.filter_by(id=_order.orderPagerID).first()
    _order_pager.active = True
    _order_pager.save()
    return redirect(url_for('pos.index'))


@pos.get('/create-order/<int:order_type_id>/<int:order_pager_id>')
def create_order(order_type_id, order_pager_id):
    _order_type = OrderType.query.filter_by(id=order_type_id).first_or_404()
    _order = Order(orderTypeID=order_type_id, orderPagerID=order_pager_id)
    _order.save()
    _order_pager = OrderPager.query.filter_by(id=order_pager_id).first_or_404()
    _order_pager.active = False
    _order_pager.save()
    return redirect(url_for('pos.order', order_number=_order.orderNumber))
