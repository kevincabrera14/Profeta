# Generated by Django 4.2.7 on 2024-03-26 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourschool', '0009_mensajes_chat_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajes_chat',
            name='usuario',
        ),
    ]
