# Generated by Django 5.1.3 on 2024-11-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='turno',
            field=models.CharField(max_length=100),
        ),
    ]
