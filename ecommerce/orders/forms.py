from django import forms
from orders.models import OrderCancellationRequest


class OrderCancellationRequestForm(forms.ModelForm):
    class Meta:
        model = OrderCancellationRequest
        fields = ["reason", "other_reason"]
