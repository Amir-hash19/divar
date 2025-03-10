from django.shortcuts import render
from django.http.response import HttpResponse

def landing_page(reqeust):
    return render(reqeust, 'product/landing.html')



def get_name(request, name):
    return HttpResponse(f"hello mr.{name}")

