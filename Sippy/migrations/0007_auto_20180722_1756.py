# Generated by Django 2.0.7 on 2018-07-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sippy', '0006_auto_20180722_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='debit_credit_cards_enabled',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='customer',
            name='did_pool_enabled',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='customer',
            name='ivr_apps_enabled',
            field=models.NullBooleanField(),
        ),
    ]
