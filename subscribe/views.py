from django.shortcuts import render
from django.contrib import messages
from .forms import SubscribeForm
from .models import Subscribe


def subscribe(request):
    subscribe_forms = SubscribeForm()
    if request.POST:
        subscribe_forms = SubscribeForm(request.POST)
        if subscribe_forms.is_valid():
            # se asegura que los datos sean correctos (cleaned_data)
            first_name = subscribe_forms.cleaned_data["first_name"]
            last_name = subscribe_forms.cleaned_data['last_name']
            email = subscribe_forms.cleaned_data['email']
            subscribe_forms = Subscribe(first_name= first_name, last_name= last_name, email=email)
            subscribe_forms.save()
            messages.success(request, 'Datos registrados')

    context = {"form": subscribe_forms}
    return render(request, 'subscribe/subscribe.html', context)
