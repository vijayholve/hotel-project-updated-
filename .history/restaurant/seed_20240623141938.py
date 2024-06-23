from django.contrib.auth.models import User
from base.models import restaurants,dish

def send_mail_to_user_after_booking( pk, id):
    
    subject = f"Your Upcoming Stay at {room.roomName}– All You Need to Know! 🌟"
    content = f"""Dear {user},


 
