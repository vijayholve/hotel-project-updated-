from django.shortcuts import render
from base.models import dish,Reviews,restaurants
def reviews_dish(reques,):
    dish_obj=dish.objects.get(id=None)
    reviews_list=Reviews.objects.filter(dish=dish_obj)
    context={}
    return render(request,"reviews/dish_reviews.html",context)


