from django.shortcuts import render
from base.models import dish,Reviews,restaurants
def reviews_dish(request,pk):
    dish_obj=dish.objects.get(id=pk)
    reviews_list=Reviews.objects.filter(dish=dish_obj)
    conte
    return render(request,"reviews/dish_reviews.html")


