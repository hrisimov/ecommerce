from celery import shared_task
from django.core.mail import send_mail

from ecommerce.settings import EMAIL_HOST_USER


@shared_task
def send_account_activation_email(message, email):
    send_mail(
        subject='Activate your account',
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=(email,),
    )
