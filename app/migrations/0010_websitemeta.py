# Generated by Django 5.0.1 on 2024-01-27 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]
