from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# from django.views.generic import DetailView


# Create your views here.

def home(request):
    context = {}
    return render(request, 'pages/index.html',context)
    
# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'pages/blog_detail.html'   

def services(request):
    return render(request, 'pages/services.html',{})

def offers(request):
    return render(request, 'pages/offers.html',{})

def contact(request):
    return render(request, 'pages/contact.html',{})

def bookings(request):
    return render(request, 'pages/booking.html',{})

# def dashboard(request):
#     return render(request, 'pages/dashboard.html')
