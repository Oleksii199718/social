from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class SubcategorySerializer(serializers.ModelSerializer):
    """Серіалізація підкатегорій"""

    class Meta:
        model = SubcategoryEvent
        exclude = ("category", "is_active")


class CategorySerializer(serializers.ModelSerializer):
    """Серіалізація категорій подій"""
    subcategory = SubcategorySerializer(many=True)

    class Meta:
        model = CategoryEvent
        fields = ("id", "category_name", "subcategory")


class UserDetailSerializer(serializers.ModelSerializer):
    """Серіалізація інформації про організатора події"""

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")


class ProfileOrganizatorSerializer(serializers.ModelSerializer):
    """Серіалізація інформації про організатора події з профелю"""

    profile = UserDetailSerializer()

    class Meta:
        model = Profile
        fields = ("id", "profile", "avatar")


class EventCategorySerializer(serializers.ModelSerializer):
    """Серіалізація категорій в події"""

    class Meta:
        model = SubcategoryEvent
        exclude = ("category", "is_active")


class EventListSerealizer(serializers.ModelSerializer):
    """Сереалізуємо всі активні події"""
    category = EventCategorySerializer(many=True)
    organizer = ProfileOrganizatorSerializer()

    class Meta:
        model = Event
        fields = ("id", "event_name", "category", "organizer", "date_event")


class EventDetailSerealizer(serializers.ModelSerializer):
    """Сереалізуємо інформацію про конкретну подію"""

    category = serializers.SlugRelatedField(slug_field="subcategory_name", read_only=True, many=True)
    organizer = UserDetailSerializer()

    class Meta:
        model = Event
        exclude = ("is_active",)


class EventCreateSerealizer(serializers.ModelSerializer):
    """Створення події"""

    class Meta:
        model = Event
        exclude = ("created", "updated")