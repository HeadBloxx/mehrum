# Generated by Django 5.1.6 on 2025-03-10 20:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrative', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mehrum',
            name='datum',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
