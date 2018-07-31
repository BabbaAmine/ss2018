# Generated by Django 2.0.7 on 2018-07-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sippy', '0004_auto_20180722_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='accounts_mgmt',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='api_access',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='api_mgmt',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customers_mgmt',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='i_commission_agent',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='i_export_type',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='i_tariff',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='payment_method',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='system_mgmt',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tariffs_mgmt',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='vouchers_mgmt',
            field=models.PositiveSmallIntegerField(default=None),
        ),
    ]