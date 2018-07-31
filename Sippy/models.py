from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class yoothUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=1000, blank=True, null=True)


    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.username



class did(models.Model):

    i_did= models.IntegerField(primary_key=True)
    did = models.CharField(max_length=200,blank=True, null=True)
    incoming_did = models.CharField(max_length=200,blank=True, null=True)
    i_ivr_application = models.IntegerField(blank=True, null=True)
    i_account = models.IntegerField(blank=True, null=True)
    i_vendor = models.IntegerField(blank=True, null=True)
    i_connection = models.IntegerField(blank=True, null=True)
    i_did_delegation=models.IntegerField(blank=True, null=True)
    delegated_to=models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.did



class customer(models.Model):

    i_customer= models.IntegerField(primary_key=True)
    balance=models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    street_addr = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mail_from = models.CharField(max_length=200)
    payment_currency = models.CharField(max_length=200)
    payment_method = models.IntegerField(blank=True, null=True)
    i_tariff = models.IntegerField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True,null=True)
    min_payment_amount =models.FloatField(blank=True,null=True)
    api_access =models.IntegerField(blank=True, null=True)
    api_mgmt =models.IntegerField(blank=True, null=True)
    i_commission_agent=models.IntegerField(blank=True, null=True)
    tariffs_mgmt =models.IntegerField(blank=True, null=True)
    vouchers_mgmt =models.IntegerField(blank=True, null=True)
    accounts_mgmt = models.IntegerField(blank=True, null=True)
    customers_mgmt = models.IntegerField(blank=True, null=True)
    system_mgmt =models.IntegerField(blank=True, null=True)
    did_pool_enabled=models.NullBooleanField(null=True)
    ivr_apps_enabled =models.NullBooleanField(null=True)
    debit_credit_cards_enabled =models.NullBooleanField(null=True)
    description = models.TextField()
    i_lang=models.CharField(max_length=200)
    i_export_type=models.IntegerField(blank=True, null=True)
    max_calls_per_second=models.FloatField(blank=True,null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class account(models.Model):

    i_account= models.IntegerField(primary_key=True)
    balance = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    street_addr = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    payment_currency = models.CharField(max_length=200)
    blocked =models.IntegerField(blank=True, null=True)
    payment_method = models.IntegerField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True,null=True)
    min_payment_amount =models.FloatField(blank=True,null=True)
    i_commission_agent=models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    i_lang=models.CharField(max_length=200)
    i_export_type=models.IntegerField(blank=True, null=True)
    max_calls_per_second=models.FloatField(blank=True,null=True)
    on_payment_action=models.IntegerField(blank=True, null=True)
    preferred_codec=models.IntegerField(blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.username


class vendor(models.Model):

    i_vendor = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    web_login=models.CharField(max_length=200,null=True,blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_addr = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    balance=models.FloatField(blank=True,null=True)
    credit_limit=models.FloatField(blank=True,null=True)
    base_currency=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    i_lang=models.CharField(max_length=200)
    i_export_type=models.IntegerField(blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class histDid(models.Model):
    i_did = models.IntegerField(primary_key=True)
    did = models.CharField(max_length=200, blank=True, null=True)
    delegated_to = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.did




