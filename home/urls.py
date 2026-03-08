from django.urls import path
from .views import (
    HomeView,
    AboutView,
    Talent,
    Portfolio,
    ContactView,
    ThankYouView
)

app_name = 'home'

urlpatterns = [

    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('talent/',Talent.as_view(), name='talent'),
    path('portfolio/',Portfolio.as_view(), name='portfolio'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('thank-you/', ThankYouView.as_view(), name='thank-you'),


]
