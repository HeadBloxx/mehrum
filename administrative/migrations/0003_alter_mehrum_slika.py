# Generated by Django 5.1.6 on 2025-03-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrative', '0002_mehrum_datum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mehrum',
            name='slika',
            field=models.ImageField(upload_to='%Y/%m/%d'),
        ),
    ]
