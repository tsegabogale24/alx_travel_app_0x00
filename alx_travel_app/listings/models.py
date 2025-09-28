#!/usr/bin/env python3
"""
Models for Listings, Bookings, and Reviews in travel app
"""

import uuid
from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
    """Represents a property listing"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.location}"


class Booking(models.Model):
    """Booking for a listing"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, related_name="bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("cancelled", "Cancelled")],
        default="pending",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.listing.title}"


class Review(models.Model):
    """Review for a listing"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing = models.ForeignKey(Listing, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # constraint can be added in validation
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.rating}/5 for {self.listing.title}"

