from django.db import models
from user_profile.models import *
from django.contrib.auth.models import User


class CategoryEvent(models.Model):
    """Модель для категорій подій"""
    category_name = models.CharField(verbose_name="Категорія події", max_length=128, blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Статус активності", default=True)

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = "Категорія події"
        verbose_name_plural = "Категорії подій"


class SubcategoryEvent(models.Model):
    """Модель для підкатегорій подій"""
    category = models.ForeignKey(CategoryEvent, verbose_name="Категорія події", related_name="subcategory", on_delete=models.CASCADE)
    subcategory_name = models.CharField(verbose_name="Підкатегорія", max_length=128, blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Статус активності", default=True)

    def __str__(self):
        return f"{self.subcategory_name}"

    class Meta:
        verbose_name = "Підкатегорія події"
        verbose_name_plural = "Підкатегорії подій"


class Event(models.Model):
    """Модель для опису події"""
    FORMAT_EVENT = [
        ("online", "online"),
        ("offline", "offline")
    ]

    event_name = models.CharField(verbose_name="Назва події", max_length=128, blank=True, null=True)
    category = models.ManyToManyField(SubcategoryEvent, verbose_name="Категорії події")
    description = models.TextField(verbose_name="Опис події", max_length=480, blank=True, null=True)
    organizer = models.ForeignKey(Profile, verbose_name="Організатор", on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="Статус активності", default=True)
    date_event = models.DateTimeField(verbose_name="Дата проведення події", auto_now=False, auto_now_add=False)
    format_event = models.CharField(verbose_name="Формат події", max_length=8, choices=FORMAT_EVENT, default="offline")
    created = models.DateTimeField(verbose_name="Дата створення події", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name="Дата оновлення події", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.event_name}"

    class Meta:
        verbose_name = "Подія"
        verbose_name_plural = "Події"
