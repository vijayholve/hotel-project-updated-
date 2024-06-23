from django.contrib.auth.models import User
from base.models import restaurants,dish

def send_mail_to_user_after_booking( pk, id):
    dish_obj=dish.objects.get(id=pk)
    user = dish_obj.user


 
