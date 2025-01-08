from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_delete_contato_delete_vip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='foto_do_cliente',
            field=models.ImageField(blank=True, null=True, upload_to='media/Clientes'),
        ),
    ]
