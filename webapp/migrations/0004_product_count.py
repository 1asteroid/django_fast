# Generated by Django 5.0.6 on 2024-06-09 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
