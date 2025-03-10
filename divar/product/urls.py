from django.urls import path
from .views import landing_page

urlpatterns = [
    path("product/",landing_page, name="landing_page"),
]