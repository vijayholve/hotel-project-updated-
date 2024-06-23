from django.contrib.auth.models import User
from base.models import restaurants,dish,orders
from django.core.mail import send_mail
from django.conf import settings

# delivery_charges
#     total_charges
#     location
#     restaurants
#     dish
#     user
def send_mail_to_user_after_booking( pk):
    order_obj=orders.objects.get(id=pk)
    user = order_obj.user
    Subject="Your Order Confirmation"

    body=fmessage = f"""
    Dear {user.username},

    Thank you for your order with {order_obj.restaurants.restaurantName}! We are delighted to inform you that your dish, {dish_name}, has been successfully placed and is now being prepared with the utmost care and attention.

    Here are the details of your order:
    - Dish Ordered: {order_obj.dish.dishName}
    - Delivery Charges: {order_obj.delivery_charges}
    - Total Charges: {order_obj.total_charges}
    - Delivery Location: {order_obj.location}

    We will notify you once your order is ready and out for delivery. Your estimated delivery time is approximately 30 minutes.

    If you have any questions or need to make changes to your order, please feel free to contact us at {sender_email}.

    Thank you for choosing {order_obj.restaurants.restaurantName}. We hope you enjoy your meal!

    Best regards,

    Your Name
    Your Position
    {order_obj.restaurants.restaurantName}
    """
    sender = settings.EMAIL_HOST_USER
    reciever=order_obj.user.email
    sendemail=send_mail(Subject,body,sender,[reciever])

    




 
