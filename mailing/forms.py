from django import forms

from .models import Message, Recipient


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = "__all__"
        exclude = ["owner"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        exclude = ["owner"]
