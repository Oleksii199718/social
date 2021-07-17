from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from user_profile.models import Profile
from django.contrib.auth.models import User


class CategoryEventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CategoryEvent._meta.fields]

    class Meta:
        model = CategoryEvent


admin.site.register(CategoryEvent, CategoryEventAdmin)


class SubcategoryEventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SubcategoryEvent._meta.fields]

    class Meta:
        model = SubcategoryEvent


admin.site.register(SubcategoryEvent, SubcategoryEventAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]
    list_display_links = ('id', 'event_name')
    search_fields = ('event_name', 'organizer__profile__username', 'organizer__profile__first_name',
                     'organizer__profile__last_name', 'organizer__profile__email')
    list_filter = ('format_event', 'is_active', 'category__category__category_name', 'category__subcategory_name')

    class Meta:
        model = Event


admin.site.register(Event, EventAdmin)
