from django.shortcuts import render
from django.views.generic import *
from django.views import View
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
import json


class UserRegistrationView(View):
    @csrf_exempt
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        user = User.objects.create_user(
                                username=body["username"],
                                password=body["password"],
                                first_name=body["first_name"],
                                last_name=body["last_name"],
                                address=body["address"],
                                phone_number=body["phone_number"],
                                status=body["status"],
                                )
        if user:
            user_data = {
                "username": body["username"],
                "password": body["password"],
                "first_name": body["first_name"],
                "last_name": body["last_name"],
                "address": body["address"],
                "phone_number": body["phone_number"],
                "status": body["status"],
            }
            return JsonResponse(user_data, safe=False)
        return HttpResponse('error while creating user!')


class UserLoginView(View):
    @csrf_exempt
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user = authenticate(request, username=body["username"], password=body["password"])

        if user is not None:
            auth.login(request, user)

            user_data = {
                "username": user.get_username(),
                "password": user.password,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "address": user.address,
                "phone_number": user.phone_number,
                "status": user.status,
            }
            return JsonResponse(user_data, safe=False)
        return HttpResponse('login unsuccessfully!')
            

class TourListView(ListView):
    model = Tour
    queryset = Tour.objects.all()

    def get(self, request, *args, **kwargs):
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        hotel_id = request.GET.get('hotel_id')
        country_id = request.GET.get('country_id')

        tours = self.filter_tours(min_price, max_price, country_id, hotel_id)

        tours_data = []
        for tour in tours:
            tours_data.append({
                'id': tour.id,
                'name': tour.name,
                'country': tour.country.name,
                'hotel': tour.hotel.name,
                'duration': tour.duration,
                'departure_date': str(tour.departure_date),
                'price': tour.price,
            })
        return JsonResponse(tours_data, safe=False)

    @staticmethod
    def filter_tours(min_price=None, max_price=None, country=None, hotel=None):
        tours = Tour.objects.all()

        filtered_tours = None

        if hotel:
            tours = tours.filter(hotel=hotel)
        if country:
            tours = tours.filter(country=country)

        if min_price is not None and max_price is not None:
            filtered_tours = tours.filter(price__gte=min_price, price__lte=max_price)
        elif min_price is not None:
            filtered_tours = tours.filter(price__gte=min_price)
        elif max_price is not None:
            filtered_tours = tours.filter(price__lte=max_price)

        if filtered_tours is not None:
            return filtered_tours
        return tours


class SpecificTourList(DetailView):
    model = Tour
    def get(self, request, *args, **kwargs):
        tour = self.get_object()
        tours_data = []
        tours_data.append({
            'id': tour.id,
            'name': tour.name,
            'country': tour.country.name,
            'hotel': tour.hotel.name,
            'duration': tour.duration,
            'departure_date': str(tour.departure_date),
            'price': tour.price,
        })
        return JsonResponse(tours_data, safe=False)


class UserListView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.status == "staff":
            users = User.objects.filter(status="client")

            users_data = []
            for user in users:
                users_data.append({
                    "id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone_number": user.phone_number,
                })
            return JsonResponse(users_data, safe=False)
        return HttpResponseNotFound("Page not found")


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            auth.logout(request)
        return HttpResponseRedirect('/tours')

def get_tours_by_country(request, country_name):
    country = Country.objects.get(name=country_name)
    tours = Tour.objects.filter(country_id=country.id)
    tours_data = []
    for tour in tours:
        tours_data.append({
            'name': tour.name,
            'hotel': tour.hotel.name,
            'country_id': country.id,
        })
    return HttpResponse(tours_data)

def get_tours_by_hotelstars(request, stars_value):
    hotels = Hotel.objects.filter(stars=stars_value)

    tours_list = []

    for hotel_ in hotels:
        tours = Tour.objects.filter(hotel=hotel_)
        tours_list.append(tours)

    tours_data = []
    for tour in tours:
        tours_data.append({
            'name': tour.name,
            'hotel': tour.hotel.name,
            'stars': tour.hotel.stars,
            'country': tour.country.name,
        })
    return HttpResponse(tours_data)


