# Generated by Django 3.1.5 on 2021-03-17 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_sellerregister_tb_status'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_tb',
            name='seller_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Admin.sellerregister_tb'),
        ),
    ]
