# Generated by Django 2.0.7 on 2018-07-22 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Sippy', '0002_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('i_vendor', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('street_addr', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('base_currency', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('i_lang', models.CharField(max_length=200)),
                ('i_export_type', models.PositiveSmallIntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
