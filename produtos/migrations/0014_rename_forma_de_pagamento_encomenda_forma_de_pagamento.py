# Generated by Django 5.1.4 on 2024-12-29 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0013_alter_encomenda_forma_de_pagamento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encomenda',
            old_name='Forma_de_Pagamento',
            new_name='forma_de_Pagamento',
        ),
    ]
