# Generated by Django 3.1.5 on 2021-01-10 05:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('individual', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
