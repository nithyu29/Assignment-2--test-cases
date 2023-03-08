from django import forms
from .models import GiftCard

class GiftCardForm(forms.ModelForm):
    class Meta:
        model = GiftCard
        fields = ['amount', 'recipient_email']
        labels = {
            'amount': 'Gift Card Amount',
            'recipient_email': 'Recipient Email'
        }
