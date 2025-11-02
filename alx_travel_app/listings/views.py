import os
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework import status
from .models import Listing, Booking, Payment, Review
from .serializers import ListingSerializer, BookingSerializer, PaymentSerializer, ReviewSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class InitiatePaymentView(views.APIView):
    def post(self, request, *args, **kwargs):
        booking_id = request.data.get('booking_id')
        amount = request.data.get('amount')
        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

        headers = {
            "Authorization": f"Bearer {os.environ.get('CHAPA_SECRET_KEY')}",
            "Content-Type": "application/json"
        }
        data = {
            "amount": amount,
            "currency": "ETB",
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "tx_ref": f"booking-{booking_id}",
            "callback_url": "http://localhost:8000/api/verify-payment/",
            "return_url": "http://localhost:3000/payment-success/"
        }

        try:
            response = requests.post("https://api.chapa.co/v1/transaction/initialize", json=data, headers=headers)
            response.raise_for_status()
            response_data = response.json()

            Payment.objects.create(
                booking=booking,
                amount=amount,
                transaction_id=response_data['data']['tx_ref'],
                payment_status='Pending'
            )

            return Response(response_data)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class VerifyPaymentView(views.APIView):
    def get(self, request, *args, **kwargs):
        tx_ref = request.query_params.get('tx_ref')
        headers = {
            "Authorization": f"Bearer {os.environ.get('CHAPA_SECRET_KEY')}"
        }

        try:
            response = requests.get(f"https://api.chapa.co/v1/transaction/verify/{tx_ref}", headers=headers)
            response.raise_for_status()
            response_data = response.json()

            if response_data['status'] == 'success':
                payment = Payment.objects.get(transaction_id=tx_ref)
                payment.payment_status = 'Completed'
                payment.save()
                # Here you would typically trigger a Celery task to send a confirmation email

            return Response(response_data)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
