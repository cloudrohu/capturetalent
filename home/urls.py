from django.urls import path
from home.views import (
    HomeView,
    AboutView,
    Talent,
    Portfolio,
    ContactView,
    ThankYouView,
    JoinNowView
)

app_name = 'home'

urlpatterns = [

    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('talent/',Talent.as_view(), name='talent'),
    path('portfolio/',Portfolio.as_view(), name='portfolio'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/', JoinNowView.as_view(), name='contact'),
    path('join-center/', JoinNowView.as_view(), name='join-center'),
    path("join-success/", ThankYouView.as_view(), name="join-success"),
    

]
