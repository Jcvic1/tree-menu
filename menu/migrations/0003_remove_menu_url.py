# Generated by Django 5.0.4 on 2024-04-10 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='url',
        ),
    ]