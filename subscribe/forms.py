from django import forms


def validate_comma(value):
    if "," in value:
        raise forms.ValidationError('El nombre no puede tener coma')
    return value


class SubscribeForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Nombre', validators=[validate_comma])
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(
        max_length=100,
        error_messages={
            'required': 'Por favor ingresa tu correo electrónico',
            'invalid': 'El correo proporcionado no es válido',
        },
        required=True)
