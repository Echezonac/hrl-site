from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home_page'),
    # path('blog/<int:pk>/',BlogDetailView.as_view(),name='detail_blog_page'),
    path('services/', services, name='service_page'),
    path('offers/', offers, name='offer_page'),
    path('contact/', contact, name='contact_page'),
    path('booking', bookings, name='booking_page'),
    # path('dash/', dashboard, name='adminPage')
]
