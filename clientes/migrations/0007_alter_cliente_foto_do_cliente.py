# Generated by Django 5.1.4 on 2025-01-14 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_cliente_numero_de_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto_do_cliente',
            field=models.ImageField(blank=True, null=True, upload_to='Clientes'),
        ),
    ]
