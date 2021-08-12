from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Customer, Address


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'First name'
        self.fields['first_name'].blank = False
        self.fields['last_name'].label = 'Last name'
        self.fields['last_name'].blank = False
        self.fields['email'].label = 'Email address'
        self.fields['email'].blank = False


class UserUpdateForm(forms.ModelForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'First name'
        self.fields['last_name'].label = 'Last name'
        self.fields['email'].label = 'Email address'
        self.fields['date_joined'].label = 'Created on'
        self.fields['last_login'].label = 'Last login'
        self.fields['date_joined'].disabled = True
        self.fields['last_login'].disabled = True


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id']


class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['customer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address_name'].disabled = True


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['customer']
