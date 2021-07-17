from django.urls import path
from . import views

urlpatterns = [
    path("category", views.CategoryEventView.as_view()),
    path("event", views.EventListView.as_view()),
    path("event/<int:pk>", views.EventDetailView.as_view()),
    path("create_event", views.EventCreateView.as_view())
]