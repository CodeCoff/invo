from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    date_of_creation = models.DateField((""), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=120)
    company_address = models.CharField( max_length=50)
    company_ph = models.IntegerField()

    def __str__(self):
        return self.name


class Items(models.Model):
    item_name = models.CharField(max_length=120)
    amount = models.BigIntegerField(default=0)  
    min_price = models.BigIntegerField()
    max_price = models.BigIntegerField()

    def __str__(self):
        return self.name


class Invoice(models.Model):
    company_name = models.CharField(max_length=120, default=" ")
    amount = models.BigIntegerField(default=0)
    purchase_date = models.DateField(null=True)
    invoice_number = models.IntegerField(default=0) 

    def __str__(self):
        return self.name
