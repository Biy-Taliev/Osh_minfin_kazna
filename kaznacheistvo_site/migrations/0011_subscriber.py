# Generated by Django 4.2.1 on 2023-07-16 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaznacheistvo_site', '0010_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]