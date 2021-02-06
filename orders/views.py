from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.urls import reverse


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            # Запуск асинхронной задачи.
            order_created.delay(order.id)
            # Сохранение заказа в сессии.
            request.session['order_id'] = order.id
            # Перенаправление на страницу оплаты.
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/checkout.html',
                  {'cart': cart, 'form': form})
