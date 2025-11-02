from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(booking_id):
    from .models import Booking
    booking = Booking.objects.get(id=booking_id)
    subject = 'Booking Confirmation'
    message = f'Dear {booking.user.username}, \n\nYour booking for {booking.hotel.name} from {booking.start_date} to \
        {booking.end_date} has been confirmed.Thank you for booking with us!'
    from_email = 'sibandallen@gmail.com'
    recipient_list = [booking.user.email]
    send_mail(subject, message, from_email, recipient_list)
