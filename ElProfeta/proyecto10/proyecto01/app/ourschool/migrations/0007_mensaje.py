# Generated by Django 4.2.7 on 2024-03-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourschool', '0006_remove_usuario_certificado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
