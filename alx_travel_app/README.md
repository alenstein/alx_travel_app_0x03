# ALX Travel App API

This project provides a Django-based API for managing property listings and bookings. It is built using the Django REST Framework and includes Swagger documentation for the API endpoints.

## Features

- CRUD operations for listings
- CRUD operations for bookings
- API documentation with Swagger
- Chapa payment integration
- Background task management with Celery and RabbitMQ
- Email notifications for bookings

## Getting Started

To get started with this project, you will need to have Python, Django, and RabbitMQ installed. You can then clone the repository and install the dependencies:

```bash
git clone https://github.com/your-username/alx_travel_app_0x03.git
cd alx_travel_app_0x03
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root of the project and add your Chapa secret key and Celery broker URL:

```
CHAPA_SECRET_KEY=your_chapa_secret_key
CELERY_BROKER_URL=amqp://guest:guest@localhost:5672//
```

Once the dependencies are installed and the environment variables are set, you can run the development server:

```bash
python manage.py runserver
```

In a separate terminal, run the Celery worker:

```bash
celery -A alx_travel_app worker -l info
```

The API will then be available at `http://127.0.0.1:8000/api/`.

## Payment Integration

This project uses the Chapa API for payment processing. The payment workflow is as follows:

1.  A user creates a booking.
2.  The user is redirected to the Chapa payment page.
3.  After the user completes the payment, Chapa sends a request to the `verify-payment` endpoint.
4.  The payment status is updated in the `Payment` model.
5.  A confirmation email is sent to the user asynchronously via a Celery background task.
