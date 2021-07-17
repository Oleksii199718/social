from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER = [
        ("male", "Чоловік"),
        ("female", "Жінка")
    ]
    profile = models.OneToOneField(User, verbose_name="Профіль", on_delete=models.CASCADE)
    gender = models.CharField(verbose_name="Стать", max_length=6, choices=GENDER, default="male")
    phone_number = models.CharField(verbose_name="Номер телефону", max_length=14)
    avatar = models.ImageField(verbose_name="Аватар", upload_to="avatar/", blank=False, null=False)
    bio = models.TextField(verbose_name="Про користувача", max_length=480, blank=False, null=False, default=None)
    birthday = models.DateField(verbose_name="Дата народження", blank=True, null=True)

    def __str__(self):
        return f"{self.profile}"

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профелі"