from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_account_activation_email(message, email):
    send_mail(
        subject='Activate your account',
        message=message,
        from_email='username@gmail.com',
        recipient_list=(email,),
    )
