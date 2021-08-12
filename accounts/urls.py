from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login_page.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='base.html'), name='logout'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/profile/', views.profile_view, name='profile_view'),
    path('accounts/profile/address/', views.AddressListView.as_view(), name='address_view'),
    path('accounts/profile/address/update/<slug:pk>', views.AddressUpdateView.as_view(), name='address_update'),
    path('accounts/profile/address/delete/<slug:pk>', views.AddressDeleteView.as_view(), name='address_delete'),
    path('accounts/profile/address/create/', views.AddressCreateView.as_view(), name='address_create'),
]
