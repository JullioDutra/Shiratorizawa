# Generated by Django 5.2.1 on 2025-05-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiratorizawa', '0005_match_confirmed_fans_match_opponent_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_subscribed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
