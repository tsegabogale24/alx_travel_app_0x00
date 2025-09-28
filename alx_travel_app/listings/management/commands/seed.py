#!/usr/bin/env python3
"""
Management command to seed the database with sample listings
"""

from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seeds the database with sample listings"

    def handle(self, *args, **options):
        sample_listings = [
            {"title": "Beach House", "description": "A house near the beach", "price_per_night": 120.00, "location": "Miami"},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains", "price_per_night": 90.00, "location": "Denver"},
            {"title": "City Apartment", "description": "Modern apartment in the city center", "price_per_night": 150.00, "location": "New York"},
        ]

        for listing_data in sample_listings:
            Listing.objects.get_or_create(**listing_data)

        self.stdout.write(self.style.SUCCESS("Database seeded with sample listings!"))
