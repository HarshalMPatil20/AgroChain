# Generated by Django 5.0.6 on 2024-10-20 11:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply_chain', '0004_storeblock'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='allowed_users',
            field=models.ManyToManyField(blank=True, related_name='allowed_crops', to=settings.AUTH_USER_MODEL),
        ),
    ]
