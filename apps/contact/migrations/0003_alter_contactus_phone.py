# Generated by Django 4.1.3 on 2022-11-26 08:06

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
