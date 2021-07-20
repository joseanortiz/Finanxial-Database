from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    client_type_choices = (
        ('Data Entry', 'Data Entry'),
        ('Reconcile and Review', 'Reconcile and Review'),
        ('Review', 'Review'),

    )

    client_name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    contact_number = PhoneNumberField()
    contact_email = models.EmailField(max_length = 200)
    contact_name_1 = models.CharField(max_length=200, blank=True)
    contact_number_1 = PhoneNumberField(blank=True)
    contact_email_1 = models.EmailField(max_length = 200, blank=True)
    client_type = models.CharField(max_length=200, choices=client_type_choices)
    industry_type = models.CharField(max_length=200, blank=True)
    project_manager = models.CharField(max_length=200, blank=True)
    tax_id = models.CharField(max_length=200)
    bank_accounts = models.CharField(max_length=200, blank=True)
    client_group = models.CharField(max_length=200)
    accounting = models.BooleanField(default=False)
    taxes = models.BooleanField(default=False)
    audits = models.BooleanField(default=False)
    tax_consulting = models.BooleanField(default=False)
    consulting = models.BooleanField(default=False)
    investment = models.BooleanField(default=False)
    planning = models.BooleanField(default=False)


    def __str__(self):
        return self.client_name



class File(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=200, blank=True)
    bank = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    document = models.FileField(upload_to='files/', blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class ClientGroup(models.Model):
    client_group = models.CharField(max_length=200)

    def __str__(self):
        return self.client_group

class Employee(models.Model):
    manager = models.CharField(max_length=200)

    def __str__(self):
        return self.manager

class Industrie(models.Model):
    industry_type_drop = models.CharField(max_length=200)

    def __str__(self):
        return self.industry_type

class Contact(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    c_name_1 = models.CharField(max_length=200, blank=True)
    c_num_1 = PhoneNumberField(blank=True)
    c_email_1 = models.EmailField(max_length=200, blank=True)
    c_name_2 = models.CharField(max_length=200, blank=True)
    c_num_2 = PhoneNumberField(blank=True)
    c_email_2 = models.EmailField(max_length=200, blank=True)
    c_name_3 = models.CharField(max_length=200, blank=True)
    c_num_3 = PhoneNumberField(blank=True)
    c_email_3 = models.EmailField(max_length=200, blank=True)
    c_name_4 = models.CharField(max_length=200, blank=True)
    c_num_4 = PhoneNumberField(blank=True)
    c_email_4 = models.EmailField(max_length=200, blank=True)
    c_name_5 = models.CharField(max_length=200, blank=True)
    c_num_5 = PhoneNumberField(blank=True)
    c_email_5 = models.EmailField(max_length=200, blank=True)

    def __str__(self):
        return self.c_name_1
