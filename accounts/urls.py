from django.urls import path

from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LogoutView, LoginView, UserDetailsView
from rest_framework_simplejwt.views import TokenVerifyView

from . import api

urlpatterns = [
    path('register/' , RegisterView.as_view(), name='rest_register'),
    path('login/' , LoginView.as_view(), name='rest_login'),
    path('logout/' , LogoutView.as_view(), name='rest_logout'),
    path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    path('myreservations/', api.ReservationsListView.as_view(), name='api_reservations_list'),
    path('<uuid:pk>/', api.LandlordView.as_view(), name='api_landlord_detail'),

]