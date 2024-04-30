import datetime
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from django.views import View

from touragency.forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import auth
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.contrib import messages
import json


class UserRegistrationView(CreateView):
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
        else:
            return render(request, 'registration_form.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'registration_form.html', {'form': form})


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login_form.html'

    def get_success_url(self):
        return reverse_lazy('home')
            

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
    def get(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated and request.user.status == "client" and Tour.objects.filter(pk=pk).exists():
            tour = Tour.objects.get(pk=pk)
            form = OrderForm()
            context = {
                'tour': tour,
                'form': form,
            }
            return render(request, 'order_create_form.html', context)
        return HttpResponseNotFound('page not found')
    
    def post(self, request, pk, *args, **kwargs):
        if request.user.is_authenticated and request.user.status == "client":
            tour = Tour.objects.get(pk=pk)

            form = OrderForm(request.POST)

            if form.is_valid():
                amount = form.cleaned_data['amount']
                departure_date = form.cleaned_data['departure_date']
                code = form.cleaned_data['promocode']

                promocode = Promocode.objects.filter(code=code).first()

                if datetime.datetime.strptime(departure_date, '%Y-%m-%d') < datetime.datetime.now() + datetime.timedelta(days=5) or amount > tour.trips:
                    return HttpResponse("Check departure date (no orders less than 5 days in advance) and amount of trips")
                else:
                    order = Order.objects.create(user=request.user, tour=tour, amount=amount, price=amount * tour.price, departure_date=departure_date)      
                    
                    if promocode:
                        order.use_discount(promocode)

                    order_data = {
                        "user": order.user.username,
                        "tour_name": order.tour.name,
                        "number": order.number,
                        "price": order.price,
                        "amount": order.amount,
                        "departure_date": order.departure_date,
                    }

                    tour.trips -= amount
                    tour.save()

                    url = reverse('user_spec_order', kwargs={"pk": order.user_id, "jk": order.number})
                    return redirect(url)
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
    
    
class SpecificOrderView(View):
    def get(self, request, pk, jk, *args, **kwargs):
        
        if request.user.is_authenticated and request.user.id==pk and Order.objects.filter(user_id=pk, number=jk).exists():
            order = Order.objects.filter(user_id=pk, number=jk).first()

            form = OrderDeleteForm()
            return render(request, 'order_delete_form.html', {'form': form, 'order': order})
        return HttpResponseNotFound("Page not found")
    
    def post(self, request, pk, jk, *args, **kwargs):
        if request.user.is_authenticated and request.user.id==pk and Order.objects.filter(user_id=pk, number=jk).exists():
            form = OrderDeleteForm(request.POST)
            if form.is_valid():
                order = Order.objects.filter(number=jk, user_id=pk).first()

                order.tour.trips += order.amount
                order.tour.save()
                order.delete()

                url = reverse('user_orders', kwargs={"pk": order.user_id})
                return redirect(url)
                    
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


class ReviewListView(ListView):
    model = Review
    queryset = Review.objects.all()
    template_name = 'reviews.html'


class ReviewCreateView(View):
    def get(self, request, **kwargs):
        if request.user.is_authenticated and request.user.status == 'client':
            form = ReviewForm()
            return render(request, 'review_create_form.html', {'form': form})
        return redirect('login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.status == 'client':
            form = ReviewForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                rating = form.cleaned_data['rating']
                text = form.cleaned_data['text']

                review = Review.objects.create(title=title, rating=rating, text=text, user=request.user)
                
                return redirect('reviews')
        return redirect('login')



class ReviewEditView(View):
    def get(self, request, pk, jk, *args, **kwargs):
        if request.user.is_authenticated and request.user.id==pk and Review.objects.filter(user_id=pk, id=jk).exists():
            review = Review.objects.filter(user_id=pk, id=jk).first()
            form = ReviewForm()
            return render(request, 'review_edit_form.html', {'form': form, 'review': review})
        return HttpResponseNotFound("Page not found")
     
    def post(self, request, pk, jk, *args, **kwargs):
        if request.user.is_authenticated and request.user.status == 'client':
            form = ReviewForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                rating = form.cleaned_data['rating']
                text = form.cleaned_data['text']
                review = Review.objects.update(title=title, rating=rating, text=text)           
                return redirect('reviews')
        return redirect('login')


#ADDITIONAL PAGES
def home(request):
    latest_article = Article.objects.latest('date')
    return render(request, 'home.html', {'latest_article': latest_article})

def about_company(request):
    info = CompanyInfo.objects.first()
    return render(request, 'about.html', {'company_info': info})

def news(request):
    news = Article.objects.all()
    return render(request, 'news.html', {'news': news})

def faqs(request):
    faqs = FAQ.objects.all()
    return render(request, 'faqs.html', {'faqs': faqs})

def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {'contacts': contacts})

def vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancies': vacancies})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})

def privacy_policy(request):
    return render(request, 'privacy.html')