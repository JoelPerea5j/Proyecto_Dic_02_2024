# Generated by Django 5.1 on 2024-11-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('id_suculsal', models.CharField(max_length=100)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('marca', models.IntegerField()),
                ('stock', models.CharField(max_length=100)),
                ('Tipo_produc', models.CharField(max_length=100)),
                ('Fecha_creacion', models.CharField(max_length=100)),
            ],
        ),
    ]