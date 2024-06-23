from django.contrib.auth.models import User
from base.models import restaurants,dish

def send_mail_to_user_after_booking( pk, id):
    dish_obj=dish.objects.get(id=pk)
    user = dish_obj.user
    Subject="Your Order Confirmation"
    body=f"""Dear {{}},

Thank you for your order with [Your Restaurant Name]! We are delighted to inform you that your dish, [Dish Name], has been successfully placed and is now being prepared with the utmost care and attention.

Here are the details of your order:

Dish Ordered: [Dish Name]
Special Instructions: [Any special instructions or notes]
We will notify you once your order is ready and out for delivery. Your estimated delivery time is approximately [Estimated Delivery Time].

If you have any questions or need to make changes to your order, please feel free to contact us at [Your Contact Information].

Thank you for choosing [Your Restaurant Name]. We hope you enjoy your meal!

Best regards,

[Your Name]
[Your Position]
[Your Restaurant Name]
[Your Contact Information]"""
    




 
