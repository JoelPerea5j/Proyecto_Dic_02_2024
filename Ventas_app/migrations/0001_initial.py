# Generated by Django 5.1.1 on 2024-11-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('Id_Ventas', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Id_Producto', models.CharField(max_length=100)),
                ('Id_Cliente', models.CharField(max_length=100)),
                ('Metodo_pago', models.CharField(max_length=100)),
                ('Fecha_Venta', models.CharField(max_length=100)),
                ('Id_empleado', models.CharField(max_length=100)),
                ('Total', models.CharField(max_length=100)),
            ],
        ),
    ]