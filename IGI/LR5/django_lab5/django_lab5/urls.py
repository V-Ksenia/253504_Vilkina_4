"""
URL configuration for django_lab5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from touragency import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.UserRegistrationView.as_view(), name="register"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    #CLIENTS
    path('tours/', views.TourListView.as_view(), name="tours"),
    path('hotels/', views.HotelListView.as_view(), name="hotels"),
    path('countries/', views.CountryListView.as_view(), name="countries"),
    path('promocodes/', views.PromocodesView.as_view(), name="promocodes"),
    path('tours/<int:pk>/', views.SpecificTourList.as_view(), name='tour'),
    path('tour/<int:pk>/order/create/', views.OrderCreateView.as_view(), name='create_order'),
    path('user/<int:pk>/orders/', views.UserOrderView.as_view(), name='user_orders'),
    path('user/<int:pk>/order/<int:jk>/', views.SpecificOrderView.as_view(), name='user_spec_order'),
    
    #STAFF
    path('users/', views.UserListView.as_view(), name='users'),
    path('orders/', views.OrderListView.as_view(), name='orders'),


    #ADDITIONAL PAGES
    path('home/', views.home, name='home'),
    path('about/', views.about_company, name='about'),
    path('news/', views.news, name='news'),
    path('faq/', views.faqs, name='terms'),
    path('contacts/', views.contacts, name='contacts'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('reviews/', views.ReviewListView.as_view(), name='reviews'),
    path('review/create/', views.ReviewCreateView.as_view(), name='add_review'),
    path('user/<int:pk>/review/<int:jk>/', views.ReviewEditView.as_view(), name='edit_review'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)