from django import forms
from .models import Review, User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'age', 'phone_number', 'address', 'password1', 'password2']

class OrderForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
    promocode = forms.CharField(max_length=10, required=False)
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class OrderDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Confirm delete', required=True)


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Review
        fields = ['title', 'rating','text']

class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']