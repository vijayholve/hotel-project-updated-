from django.urls import path
from base.models import Reviews 
from . import views 
urlpatterns = [
    path("",views.reviews_dish,name="reviews-dish"),
]




