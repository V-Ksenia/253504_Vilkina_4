import datetime
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

        age =body["age"]

        if age < 18:
            return HttpResponse('Your age must be greater than 17!')
        else:
            user = User.objects.create_user(
                                    username=body["username"],
                                    password=body["password"],
                                    first_name=body["first_name"],
                                    last_name=body["last_name"],
                                    age=body["age"],
                                    address=body["address"],
                                    phone_number=body["phone_number"],
                                    status=body["status"],
                                    )
            
            if user:
                user_data = {
                    "username": user.username,
                    "password": user.password,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": user.age,
                    "address": user.address,
                    "phone_number": user.phone_number,
                    "status": user.status,
                }
                return JsonResponse(user_data, safe=False)
        return HttpResponse('User registration failed')


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
                "age": user.age,
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
                'duration_weeks': tour.duration,
                'price': tour.get_price(),
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
            'country_climate': list(tour.country.climate.all().values_list('climate', flat=True)),
            'hotel': tour.hotel.name,
            'hotel_stars': tour.hotel.stars,
            'duration_weeks': tour.duration,
            'price': tour.price,
            'amount_of_trips': tour.trips,
        })
        return JsonResponse(tours_data, safe=False)


class HotelListView(ListView):
    model = Hotel
    queryset = Hotel.objects.all()

    def get(self, request, *args, **kwargs):
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        country_id = request.GET.get('country_id')
        stars_value = request.GET.get('stars')

        hotels = self.filter_hotels(min_price, max_price, country_id, stars_value)

        hotels_data = []
        for hotel in hotels:
            hotels_data.append({
                'id': hotel.id,
                'name': hotel.name,
                'stars': hotel.stars,
                'country': hotel.country.name,
                'price_per_night': hotel.price_per_night,
            })
        return JsonResponse(hotels_data, safe=False)

    @staticmethod
    def filter_hotels(min_price=None, max_price=None, country=None, stars=None):
        hotels = Hotel.objects.all()

        filtered_hotels = None
        if stars:
            hotels = hotels.filter(stars=stars)
        if country:
            hotels = hotels.filter(country=country)

        if min_price is not None and max_price is not None:
            filtered_hotels = hotels.filter(price_per_night__gte=min_price, price__lte=max_price)
        elif min_price is not None:
            filtered_hotels = hotels.filter(price_per_night__gte=min_price)
        elif max_price is not None:
            filtered_hotels = hotels.filter(price_per_night__lte=max_price)

        if filtered_hotels is not None:
            return filtered_hotels
        return hotels
    

class CountryListView(ListView):
    def get(self, request, *args, **kwargs):
       
        countries = Country.objects.all()

        countries_data = []
        for country in countries:
            climates = list(country.climate.all().values_list('climate', flat=True))

            countries_data.append({
                'id': country.id,
                'name': country.name,
                'climate': climates,
            })
        return JsonResponse(countries_data, safe=False)
    

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
                    "age": user.age,
                    "phone_number": user.phone_number,
                })
            return JsonResponse(users_data, safe=False)
        
        return HttpResponseNotFound("For staff only")


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            auth.logout(request)
        return HttpResponseRedirect('/tours')


class OrderCreateView(View):
    def post(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated and request.user.status == "client":
            tour = Tour.objects.get(pk=pk)

            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            amount = body["amount"]
            departure_date = body["departure_date"]
            code = body["promocode"]
            promocode = Promocode.objects.filter(code=code).first()

            if datetime.datetime.strptime(departure_date, '%Y-%m-%d') < datetime.datetime.now() + datetime.timedelta(days=5) or amount > tour.trips:
                return HttpResponseNotFound("Check departure date (no orders less than 5 days in advance) and amount of trips")
            else:
                order = Order.objects.create(user=request.user, tour=tour, amount=amount,
                                            price=amount * tour.price, departure_date=departure_date)      
                if promocode:
                    order.use_discount(promocode)

                order_data = {
                    "user": order.user.username,
                    "tour_id": order.tour.id,
                    "number": order.number,
                    "price": order.price,
                    "amount": order.amount,
                    "departure_date": order.departure_date,
                }

                tour.trips -= amount
                tour.save()
                
                return JsonResponse(order_data, safe=False)
        elif request.user.is_authenticated and request.user.status == "staff":
            return HttpResponseNotFound("For clients only")
        else:
            return HttpResponse('Sign in to make an order')


class UserOrderView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        
        if request.user.is_authenticated and request.user.id==pk:
            orders = Order.objects.filter(user_id=pk)

            orders_data = []
            for order in orders:
                orders_data.append({
                    "user": order.user.username,
                    "number": order.number,
                    "tour_name": order.tour.name,
                    "price": order.price,
                    "amount": order.amount,
                    "departure_date": order.departure_date,
                })

            return JsonResponse(orders_data, safe=False)
       
        return HttpResponseNotFound("Page not found")
    

class OrderListView(View):
    def get(self, request, *args, **kwargs):      
        if request.user.is_authenticated and request.user.status == "staff":
            orders = Order.objects.all()

            orders_data = []
            for order in orders:
                orders_data.append({
                    "user": order.user.username,
                    "first_name": order.user.first_name,
                    "phone_number": order.user.phone_number,
                    "number": order.number,
                    "tour_name": order.tour.name,
                    "price": order.price,
                    "amount": order.amount,
                    "departure_date": order.departure_date,
                })
            return JsonResponse(orders_data, safe=False)
        
        return HttpResponseNotFound("Page not found")


class PromocodesView(View):
    def get(self, request, *args, **kwargs):
        codes = Promocode.objects.all()
        codes_data = []

        for code in codes:
            codes_data.append({
                "code": code.code,
                "discount": code.discount,
            })
        return JsonResponse(codes_data, safe=False)



#ADDITIONAL PAGES
def home(request):
    latest_article = Article.objects.latest('published_date')
    return render(request, 'home.html', {'latest_article': latest_article})

def about_company(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'about.html', {'company_info': company_info})

def news(request):
    all_news = News.objects.all()
    return render(request, 'news.html', {'all_news': all_news})

def terms(request):
    all_terms = Term.objects.all()
    return render(request, 'terms.html', {'all_terms': all_terms})

def contacts(request):
    all_contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'all_contacts': all_contacts})

def vacancies(request):
    all_vacancies = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'all_vacancies': all_vacancies})

def reviews(request):
    all_reviews = Review.objects.all()
    return render(request, 'reviews.html', {'all_reviews': all_reviews})

def privacy_policy(request):
    return render(request, 'privacy.html')