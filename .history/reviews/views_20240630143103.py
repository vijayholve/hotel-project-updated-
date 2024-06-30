from django.shortcuts import render
from base.models import dish,Reviews,restaurants
from django import template
from django.utils import timezone
    
def reviews_dish(request,pk):
    dish_obj=dish.objects.get(id=pk)
    reviews_list=Reviews.objects.filter(dish=dish_obj)
    context={"dish_obj":dish_obj,"reviews_list":reviews_list}
    return render(request,"reviews/dish_reviews.html",context)

def time_since(value):
    now=timezone.now()
    
