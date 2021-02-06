from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField(label="Promo code", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
