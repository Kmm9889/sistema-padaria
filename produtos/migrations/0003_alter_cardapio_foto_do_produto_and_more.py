# Generated by Django 5.1.4 on 2024-12-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_rename_disponibilidade_cardapio_novidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='foto_do_produto',
            field=models.ImageField(blank=True, null=True, upload_to='media/Cardapio'),
        ),
        migrations.AlterField(
            model_name='encomenda',
            name='foto_do_Produto_Encomendado',
            field=models.ImageField(blank=True, null=True, upload_to='media/Encomendas'),
        ),
    ]
