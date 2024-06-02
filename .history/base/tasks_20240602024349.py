from celery import shared_task
from .seed import register_user_to_send_mail
import datetime
@shared_task(bind=True)
def send_mail_task(self,email,fullname):
    register_user_to_send_mail([email],fullname)
    times=datetime.datetime.now()
    current_time = times.strftime("%Y-%m-%d %H:%M:%S")
    return f"procced at {current_time} "
def send_mail_to_all_task(self):
    pass