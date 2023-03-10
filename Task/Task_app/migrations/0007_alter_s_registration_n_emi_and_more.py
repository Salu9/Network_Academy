# Generated by Django 4.1.5 on 2023-01-25 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Task_app', '0006_s_registration_delete_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s_registration',
            name='n_emi',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='s_registration',
            name='s_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
