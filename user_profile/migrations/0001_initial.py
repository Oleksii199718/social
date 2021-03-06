# Generated by Django 3.1.7 on 2021-03-13 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Чоловік'), ('female', 'Жінка')], default='male', max_length=6, verbose_name='Стать')),
                ('phone_number', models.CharField(max_length=14, verbose_name='Номер телефону')),
                ('avatar', models.ImageField(upload_to='media/avatar/', verbose_name='Аватар')),
                ('bio', models.TextField(default=None, max_length=480, verbose_name='Про користувача')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата народження')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Профіль')),
            ],
            options={
                'verbose_name': 'Профіль',
                'verbose_name_plural': 'Профелі',
            },
        ),
    ]
