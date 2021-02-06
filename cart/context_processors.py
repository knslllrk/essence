from .cart import Cart
from coupons.forms import CouponApplyForm


def cart(request):
    '''for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'update': True})'''
    coupon_apply_form = CouponApplyForm()
    return {'cart': Cart(request), 'coupon_apply_form': coupon_apply_form}
