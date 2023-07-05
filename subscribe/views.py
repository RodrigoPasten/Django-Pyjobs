from django.shortcuts import render
from django.contrib import messages
from .forms import SubscribeForm
from .models import Subscribe


def subscribe(request):
    subscribe_forms = SubscribeForm()
    if request.POST:
        subscribe_forms = SubscribeForm(request.POST)
        if subscribe_forms.is_valid():
            # guarda los datos del modelform (forms.py)
            subscribe_forms.save()

    context = {"form": subscribe_forms}
    return render(request, 'subscribe/subscribe.html', context)
