from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = "__all__"
        labels = {
            'first_name': _('Ingrese su nombre'),
            'last_name': _('Su apellido aqui'),
            'email': _('Acá, su email')
        }


