# Generated by Django 2.2.1 on 2019-05-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='preco',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=25.99, max_digits=7, verbose_name='Preço'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantidade'),
        ),
    ]
