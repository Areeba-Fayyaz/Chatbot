# Generated by Django 4.2.7 on 2023-11-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_chatmessage_delete_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='is_bot',
            field=models.BooleanField(default=False),
        ),
    ]
