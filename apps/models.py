from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    detail = models.CharField(max_length=1024)
    phone_no = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=15)
    is_valid = models.BooleanField(default=True)

class Order(models.Model):
    # sender information
    sender_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=40)
    sender = models.ForeignKey(User, blank=True, null=True)

    # recipient information
    recipient_name = models.CharField(max_length=30)
    from_address = models.ForeignKey(Address)
    from_phone_no = models.CharField(max_length=30)
    to_address = models.ForeignKey(Address)
    to_phone_no = models.CharField(max_length=30)
    PAYMENT_CHOICES = (
        ('S', 'By sender'),
        ('R', 'By recipient'),
        ('C', 'Company Account')
    )
    payment_type = models.CharField(choices=PAYMENT_CHOICES)

    DELIVERY_CHOICES = (
        ('E', 'Express(3-7 Work Days'),
        ('R', 'Regular(20-30 Work Days')
    )
    delivery_type = models.CharField(choices=DELIVERY_CHOICES)

    # charge information
    trans_charge = models.FloatField(default=0.0)
    duty = models.FloatField(default=0.0)

    # date/authorized by
    accept_by = models.ForeignKey(User)
    accept_time = models.DateTimeField()

    creation_time = models.DateTimeField()
    tracking_no = models.CharField(max_length=20)

class Package(models.Model):
    order = models.ForeignKey(Order)
    # package information
    PACKING_CHOICES = (
        ('D', 'Document'),
        ('P', 'Package'),
        ('O', 'Other')
    )
    packing = models.CharField(choices=PACKING_CHOICES)

    # dimention information (in cm)
    length = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)

    # weight (in kg)
    weight = models.FloatField(default=0.0)

class Item(models.Model):
    package = models.ForeignKey(Package)
    description = models.CharField(max_length=50)
    harmonized_code = models.CharField(max_length=10)
    manu_country = models.CharField(max_length=30)
    quantity = models.DecimalField(default=1)
    unit_price = models.FloatField(default=-1)
    
    is_sed_attached = models.BooleanField(default=False)
