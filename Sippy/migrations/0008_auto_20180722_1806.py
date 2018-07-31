# Generated by Django 2.0.7 on 2018-07-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sippy', '0007_auto_20180722_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='accounts_mgmt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='api_access',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='api_mgmt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='credit_limit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customers_mgmt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='i_commission_agent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='i_export_type',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='i_tariff',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='max_calls_per_second',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='min_payment_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='payment_method',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='system_mgmt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tariffs_mgmt',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='vouchers_mgmt',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]