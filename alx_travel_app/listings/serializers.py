#!/usr/bin/env python3
"""
Serializers for Listings and Bookings
"""

from rest_framework import serializers
from .models import Listing, Booking, Review


class ListingSerializer(serializers.ModelSerializer):
    """Serializer for Listing model with nested reviews"""
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = ["id", "title", "description", "price_per_night", "location", "created_at", "reviews"]

    def get_reviews(self, obj):
        return [{"user": r.user.username, "rating": r.rating, "comment": r.comment} for r in obj.reviews.all()]


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    listing = serializers.CharField(source="listing.title", read_only=True)
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "listing", "user", "start_date", "end_date", "status", "created_at"]
