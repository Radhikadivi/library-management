# Generated by Django 3.2.25 on 2024-04-02 12:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Book',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateTimeField(default=datetime.datetime(2024, 4, 2, 12, 48, 23, 214712, tzinfo=utc))),
                ('returned_date', models.DateTimeField(default=datetime.datetime(2024, 4, 2, 12, 48, 23, 214712, tzinfo=utc))),
                ('renewal_count', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowing_book', to='studentapp.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowing_student', to='studentapp.student')),
            ],
        ),
    ]