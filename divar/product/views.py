from django.shortcuts import render

def landing_page(reqeust):
    return render(reqeust, 'product/landing.html')