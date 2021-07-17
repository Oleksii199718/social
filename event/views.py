import permission as permission
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import (EventListSerealizer,
                          EventDetailSerealizer,
                          EventCreateSerealizer,
                          CategorySerializer)


class CategoryEventView(APIView):
    """Виводимо категорії та підкатегорії подій"""

    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        category = CategoryEvent.objects.filter(is_active=True)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class EventListView(APIView):
    """Виводимо список активних подій"""
    def get(self, request):
        events = Event.objects.filter(is_active=True)
        serializer = EventListSerealizer(events, many=True)
        return Response(serializer.data)


class EventDetailView(APIView):
    """Виводимо інформацію про подію"""
    def get(self, request, pk):
        event = Event.objects.get(id=pk, is_active=True)
        serializer = EventDetailSerealizer(event)
        return Response(serializer.data)


class EventCreateView(APIView):
    """Створення події"""
    def post(self, request):
        event = EventCreateSerealizer(data=request.data)
        if event.is_valid():
            event.save()
            return Response(status=201)
        else:
            return Response(status=400)


