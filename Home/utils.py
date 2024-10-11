from django.conf  import settings
from django.core.mail import send_mail


def send_email():
    subject = "this i a test email"
    message = "Test12345"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["saimaniroopm@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)



