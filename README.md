# Overview
This task focuses on enhancing the alx_travel_app project by implementing asynchronous background processing using Celery with RabbitMQ as the message broker. The main feature added is an email notification system that sends booking confirmations without blocking the main request-response cycle. This ensures improved performance and a better user experience.

## Learning Objectives
By completing this task, learners will:

- Understand how to integrate Celery with RabbitMQ in a Django application.
- Learn to configure asynchronous task processing for improved performance.
- Implement an email notification feature triggered by user actions.
- Gain experience in working with Django’s email backend for automated communications.

## Learning Outcomes
After completing this task, learners will be able to:

- Configure and run Celery with RabbitMQ as a message broker.
- Create and manage shared tasks in Django using Celery.
- Trigger Celery tasks from Django views or viewsets.
- Test and verify asynchronous operations such as sending emails.

## Key Concepts
- Asynchronous Task Processing: Running time-consuming tasks in the background.
- Message Broker: Middleware (RabbitMQ) used to send and receive task messages between Django and Celery.
- Celery Configuration: Setting up celery.py and integrating it into settings.py.
- Shared Tasks: Functions decorated with @shared_task for execution by Celery workers.
- Email Backend in Django: Configuring SMTP settings for sending automated emails.

## Tools and Libraries
- Django – Backend web framework for building the application.
- Celery – Distributed task queue for background task execution.
- RabbitMQ – Message broker to handle communication between Django and Celery.
- SMTP Email Backend – For sending booking confirmation emails.
- 
