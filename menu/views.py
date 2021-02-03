from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza


def menu(request):
    pizza_all = Pizza.objects.all().order_by('prix')
    context = {'pizzas': pizza_all}
    return render(request, 'menu/listpizza.html', context)


def api_get_pizzas(request):
    pizza_all = Pizza.objects.all().order_by('prix')
    json = serializers.serialize("json", pizza_all)
    return HttpResponse(json)
