from django.contrib.auth.models import User
from base.models import restaurants,dish

def send_mail_to_user_after_booking( pk, id):
    room = Room.objects.get(id=pk)
    booking = Booking.objects.get(id=id)
    user = booking.user
    subject = f"Your Upcoming Stay at {room.roomName}– All You Need to Know! 🌟"
    content = f"""Dear {user},


 
