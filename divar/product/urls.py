from django.urls import path
from .views import landing_page,get_name

urlpatterns = [
    path("product/",landing_page, name="landing_page"),
    path("product/intro/<str:name>", get_name),
    
]