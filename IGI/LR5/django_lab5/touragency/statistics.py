from datetime import datetime
from urllib import parse

from django.http import HttpResponseNotFound
import numpy as np
from statistics import median, mode, mean
import matplotlib
from django.db.models import Sum, Count

from .models import *
from matplotlib import pyplot as plt
from django.shortcuts import render

def clients(request): 
    if request.user.is_authenticated and request.user.is_superuser:   
        clients = User.objects.filter(status='client').order_by('first_name')
        ages = []
        for client in clients:
            ages.append(client.age)

        average_age = round(mean(ages), 2)
        median_age = round(median(ages), 2)

        return render(request, 'clients_stat.html', {'clients': clients,
                                                'average_age': average_age,
                                                'median_age': median_age,
                                                })
    return HttpResponseNotFound("Page not found")


def tours(request):
    if request.user.is_authenticated and request.user.is_superuser: 
        tours = Tour.objects.all().order_by('name')
        
        tour_orders = Order.objects.values('tour__name').annotate(order_count=Count('tour__name')).order_by('-order_count')
        most_popular_tours = tour_orders.first()

        return render(request, 'tours_stat.html', {'tours': tours,
                                                'most_popular_tour': most_popular_tours,
                                                })
    
    return HttpResponseNotFound("Page not found")


def sales(request):
    if request.user.is_authenticated and request.user.is_superuser: 
        orders = Order.objects.all()
        prices = []
        general_sales = 0.0
        for order in orders:
            prices.append(order.price)
            general_sales += order.price
    
        average_sales = round(mean(prices), 2)
        median_sales = round(median(prices), 2)
        mode_sales = round(mode(prices), 2)

        return render(request, 'sales_stat.html', {'general_sales': general_sales,
                                                'average_sales': average_sales,
                                                'median_sales': median_sales,
                                                'mode_sales': mode_sales,
                                                })
    return HttpResponseNotFound("Page not found")