# Generated by Django 5.1.4 on 2024-12-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_volunteer_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Admin_Response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
