# Generated by Django 4.2 on 2023-05-01 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kaznacheistvo_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsdetails',
            name='newsObject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kaznacheistvo_site.news'),
            preserve_default=False,
        ),
    ]
