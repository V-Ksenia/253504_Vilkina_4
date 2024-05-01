from django.test import TestCase, Client
from django.urls import reverse
from .models import Tour, Promocode, Order
from .forms import OrderForm
from django.contrib.auth.models import User
from touragency.views import *


class OrderCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.country = Country.objects.create(name="name")
        self.hotel = Hotel.objects.create(name="hotel", stars=5, country_id=1, price_per_night=100)
        self.user_client = User.objects.create_user(username='client', password='password', status='client', phone_number = "+375(29)1214121", first_name = "Hdhdj", last_name="djksjdk", address = "ul.shjhds1", age=30)
        self.user_staff = User.objects.create_user(username='staff', password='password', status='staff', phone_number = "+375(29)1214223", first_name = "Afjdfj", last_name="Hjhxd", address = "ul.shjhds132", age=20)
        self.tour = Tour.objects.create(name='Test Tour', trips=10, price=100, country_id=1, hotel_id=1, duration=2)
        self.promocode = Promocode.objects.create(code='TEST123', discount=10)

    def test_get_create_order_view_authenticated_client_tour_exists(self):
        self.client.force_login(self.user_client)
        response = self.client.get(reverse('create_order', kwargs={'pk': self.tour.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_create_form.html')

    def test_get_create_order_view_authenticated_client_tour_does_not_exist(self):
        self.client.force_login(self.user_client)
        response = self.client.get(reverse('create_order', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)

    def test_get_create_order_view_authenticated_staff(self):
        self.client.force_login(self.user_staff)
        response = self.client.get(reverse('create_order', kwargs={'pk': self.tour.pk}))
        self.assertEqual(response.status_code, 404)

    def test_get_create_order_view_unauthenticated(self):
        response = self.client.get(reverse('create_order', kwargs={'pk': self.tour.pk}))
        self.assertEqual(response.status_code, 404)  # Assuming it redirects to login page or displays a message

    def test_post_create_order_view_authenticated_client_valid_data(self):
        self.client.force_login(self.user_client)
        data = {
            'amount': 2,
            'departure_date': '2024-07-01',
            'promocode': 'TEST123'
        }
        response = self.client.post(reverse('create_order', kwargs={'pk': self.tour.pk}), data)
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after successful order creation

    def test_post_create_order_view_authenticated_client_invalid_data(self):
        self.client.force_login(self.user_client)
        data = {
            'amount': 20,  # More than available trips
            'departure_date': '2024-05-01',
            'promocode': 'TEST123'
        }
        response = self.client.post(reverse('create_order', kwargs={'pk': self.tour.pk}), data)
        self.assertEqual(response.status_code, 200) 

    def test_post_create_order_view_authenticated_staff(self):
        self.client.force_login(self.user_staff)
        response = self.client.post(reverse('create_order', kwargs={'pk': self.tour.pk}))
        self.assertEqual(response.status_code, 404)

    def test_post_create_order_view_unauthenticated(self):
        response = self.client.post(reverse('create_order', kwargs={'pk': self.tour.pk}))
        self.assertEqual(response.status_code, 200) 
