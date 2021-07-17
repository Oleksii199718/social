from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile
from event.models import Event


class EventInline(admin.TabularInline):
    model = Event
    extra = 0
    can_delete = False
    show_change_link = True
    fk_name = 'organizer'
    readonly_fields = ('event_name', 'category', 'format_event', 'date_event', 'is_active')
    exclude = ('description',)
    ordering = ('-date_event',)
    verbose_name = "Організована користувачем подія"
    verbose_name_plural = "Організовані користувачем події"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "profile", "phone_number", "get_image")
    list_display_links = ('id', 'profile')
    readonly_fields = ("get_image",)
    list_filter = ('gender',)
    search_fields = ('phone_number', 'profile__username', 'profile__first_name', 'profile__last_name',
                     'profile__email')
    save_on_top = True
    inlines = [EventInline]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="50" height="50">')

    get_image.short_description = "Аватар"

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileAdmin)
