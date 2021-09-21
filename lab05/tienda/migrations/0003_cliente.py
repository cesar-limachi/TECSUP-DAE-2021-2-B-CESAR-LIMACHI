# Generated by Django 3.2.6 on 2021-09-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=8)),
                ('telefono', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=100)),
                ('fecha_nacimiento', models.DateTimeField(verbose_name='fecha de nacimiento')),
                ('fecha_publicacion', models.DateTimeField(verbose_name='fecha de publicacion')),
            ],
        ),
    ]