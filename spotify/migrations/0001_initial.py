# Generated by Django 3.2.6 on 2021-11-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('refresh_token', models.CharField(max_length=150)),
                ('access_token', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('token_type', models.CharField(max_length=50)),
            ],
        ),
    ]
