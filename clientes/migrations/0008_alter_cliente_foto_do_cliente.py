# Generated by Django 5.1.4 on 2025-01-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_alter_cliente_foto_do_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto_do_cliente',
            field=models.ImageField(blank=True, null=True, upload_to='Clientes/'),
        ),
    ]