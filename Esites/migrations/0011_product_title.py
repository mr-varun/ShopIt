# Generated by Django 4.1.7 on 2023-06-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esites', '0010_alter_product_amazon_link_alter_product_amazon_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
