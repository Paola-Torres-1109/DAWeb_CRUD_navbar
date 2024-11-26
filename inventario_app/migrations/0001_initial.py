# Generated by Django 5.1 on 2024-11-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('vehiculo', models.CharField(max_length=100)),
                ('cantidad_auto', models.BigIntegerField()),
                ('ubicacion', models.CharField(max_length=100)),
                ('estado_bmr', models.CharField(max_length=100)),
                ('proveedor', models.CharField(max_length=100)),
            ],
        ),
    ]
