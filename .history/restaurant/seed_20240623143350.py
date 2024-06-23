from django.contrib.auth.models import User
from base.models import restaurants,dish,orders

def send_mail_to_user_after_booking( pk):
    order_obj=orders.objects.get(id=pk)
    user = dish_obj.user
    Subject="Your Order Confirmation"
    delivery_charges
total_charges
location
restaurants
dish
user
    body=fmessage = f"""
    Dear {orders},

    Thank you for your order with {restaurant_name}! We are delighted to inform you that your dish, {dish_name}, has been successfully placed and is now being prepared with the utmost care and attention.

    Here are the details of your order:
    - Dish Ordered: {dish_name}
    - Delivery Charges: {delivery_charges}
    - Total Charges: {total_charges}
    - Delivery Location: {location}

    We will notify you once your order is ready and out for delivery. Your estimated delivery time is approximately 30 minutes.

    If you have any questions or need to make changes to your order, please feel free to contact us at {sender_email}.

    Thank you for choosing {restaurant_name}. We hope you enjoy your meal!

    Best regards,

    Your Name
    Your Position
    {restaurant_name}
    """

    




 
