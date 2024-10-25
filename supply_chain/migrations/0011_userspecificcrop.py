# Generated by Django 5.0.6 on 2024-10-24 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply_chain', '0010_crop_specific_user_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSpecificCrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specific_price', models.FloatField()),
                ('allowed', models.BooleanField(default=True)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_specifics', to='supply_chain.crop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
