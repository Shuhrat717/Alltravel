# Generated by Django 4.1.3 on 2022-12-07 17:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_alter_contactus_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='email',
        ),
        migrations.AddField(
            model_name='contactus',
            name='facebook',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='instagram',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
