from django.urls import path
from .views import download_cookies,print_page_user
urlpatterns = [
    path("cookies/", download_cookies),
    path("register/", print_page_user),
]