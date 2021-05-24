from django.db import models


class Client(models.Model):
    client_type_choices = (
        ('Data Entry', 'Data Entry'),
        ('Reconcile and Review', 'Reconcile and Review'),
        ('Review', 'Review'),

    )

    client_name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length = 200)
    client_type = models.CharField(max_length=200, choices=client_type_choices)
    industry_type = models.CharField(max_length=200)
    project_manager = models.CharField(max_length=200)
    tax_id = models.CharField(max_length=200)
    bank_accounts = models.CharField(max_length=200)
    client_group = models.CharField(max_length=200)


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
