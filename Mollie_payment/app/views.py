from django.shortcuts import render

# Create your views here.

def chargebee(request):
    
    return render(request, "app/chargebee.html")

def chargebee1(request):
    return render(request, "app/chargebee1.html")

def chargebee2(request):
    return render(request, "app/chargebee2.html")