# Generated by Django 5.2 on 2025-04-14 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='status',
        ),
    ]
