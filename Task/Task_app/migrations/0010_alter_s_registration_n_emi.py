# Generated by Django 4.1.5 on 2023-01-26 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task_app', '0009_alter_s_registration_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s_registration',
            name='n_emi',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
