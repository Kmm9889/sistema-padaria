# Generated by Django 5.1.4 on 2025-01-14 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_alter_produto_foto_do_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto_do_produto',
            field=models.ImageField(blank=True, null=True, upload_to='Cardapio'),
        ),
    ]
