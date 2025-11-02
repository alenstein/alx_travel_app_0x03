from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **options):
        self.stdout.write('Seeding the database...')

        # Clear existing data
        Listing.objects.all().delete()

        # Create sample listings
        listings_data = [
            {
                'title': 'Cozy Apartment in the Heart of the City',
                'description': 'A beautiful and cozy apartment located in the city center.',
                'price': 150.00,
                'address': '123 Main St',
                'country': 'USA',
                'city': 'New York',
            },
            {
                'title': 'Modern Loft with Stunning Views',
                'description': 'A modern loft with breathtaking views of the city skyline.',
                'price': 200.00,
                'address': '456 High St',
                'country': 'USA',
                'city': 'Los Angeles',
            },
            {
                'title': 'Charming Cottage by the Sea',
                'description': 'A charming cottage just a few steps from the beach.',
                'price': 120.00,
                'address': '789 Ocean Ave',
                'country': 'USA',
                'city': 'Miami',
            },
        ]

        for data in listings_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
