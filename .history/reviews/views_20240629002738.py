from django.shortcuts import render
from base.models import dish,Reviews,restaurants
def reviews_dish(request,pk):
    dish_obj=dish.objects.get(id=pk)
    


