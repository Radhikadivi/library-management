# Generated by Django 3.2.25 on 2024-04-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_auto_20240403_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='borrowed_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='borrowing',
            name='returned_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
