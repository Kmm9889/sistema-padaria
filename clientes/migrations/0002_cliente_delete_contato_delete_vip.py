# Generated by Django 5.1.4 on 2024-12-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('avaliação_da_padaria', models.TextField()),
                ('Cartão_Fidelidade', models.BooleanField()),
                ('foto_do_cliente', models.ImageField(blank=True, null=True, upload_to='Cliente')),
            ],
        ),
        migrations.DeleteModel(
            name='Contato',
        ),
        migrations.DeleteModel(
            name='Vip',
        ),
    ]