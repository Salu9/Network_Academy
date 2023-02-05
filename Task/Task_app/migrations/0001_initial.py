# Generated by Django 4.1.5 on 2023-01-25 17:05

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
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('reg_no', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('paddress', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('dob', models.CharField(max_length=255)),
                ('b_group', models.CharField(max_length=255)),
                ('g_name', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('g_number', models.IntegerField()),
                ('course', models.CharField(max_length=255)),
                ('course_fee', models.IntegerField()),
                ('p_mode', models.CharField(max_length=255)),
                ('n_emi', models.IntegerField()),
                ('student_Photo', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('s_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
