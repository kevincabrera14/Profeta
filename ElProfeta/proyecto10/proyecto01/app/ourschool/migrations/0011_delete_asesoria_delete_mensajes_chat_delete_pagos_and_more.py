# Generated by Django 5.0.4 on 2024-05-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourschool', '0010_remove_mensajes_chat_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='asesoria',
        ),
        migrations.DeleteModel(
            name='Mensajes_chat',
        ),
        migrations.DeleteModel(
            name='pagos',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.IntegerField(choices=[(1, 'admin'), (3, 'docente')]),
        ),
    ]
