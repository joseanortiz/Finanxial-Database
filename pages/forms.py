from django import forms
from .models import Client, File, ClientGroup, Employee, Industrie, Contact
from phonenumber_field.formfields import PhoneNumberField

class ClientForm(forms.ModelForm):
    accounting = forms.BooleanField(required=False)
    taxes = forms.BooleanField(required=False)
    audits = forms.BooleanField(required=False)
    tax_consulting = forms.BooleanField(required=False)
    consulting = forms.BooleanField(required=False)
    investment = forms.BooleanField(required=False)
    planning = forms.BooleanField(required=False)
    contact_number = PhoneNumberField()
    contact_number_1 = PhoneNumberField(required=False)
    class Meta:
        model = Client
        fields = ['client_name', 'contact_name', 'contact_number', 'contact_email', 'contact_name_1', 'contact_number_1', 'contact_email_1',  'client_type', 'industry_type',
                'project_manager', 'tax_id', 'bank_accounts', 'client_group', 'accounting', 'taxes', 'audits', 'tax_consulting', 'consulting',  'investment', 'planning']
        labels = {
        'client_name': '',
        'contact_name': '',
        'contact_number': '',
        'contact_email': '',
        'contact_name_1': '',
        'contact_number_1': '',
        'contact_email_1': '',
        'client_type': '',
        'industry_type': '',
        'project_manager': '',
        'tax_id': '',
        'bank_accounts': '',
        'client_group': '',
        'accounting': '',
        'taxes': '',
        'audits': '',
        'tax_consulting': '',
        'consulting': '',
        'investment': '',
        'planning': '',
        }
        widgets = {
            'client_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Client Name'}),
            'contact_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Name' }),
            'contact_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'contact_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Contact Email'}),
            'contact_name_1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Name' }),
            'contact_number_1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'contact_email_1': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Contact Email'}),
            'client_type': forms.Select(attrs={'class':'form-control'}),
            'industry_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Industry Type'}),
            'project_manager': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Manager'}),
            'tax_id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tax ID'}),
            'bank_accounts': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank Accounts'}),
            'client_group': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Client Group'}),
        }


class FileForm(forms.ModelForm):
    completed = forms.BooleanField(required=False)
    class Meta:
        model = File
        fields = ['client', 'document_type', 'bank', 'description', 'document', 'completed']
        labels = {
        'client': '',
        'document_type': '',
        'bank': '',
        'description': '',
        'document': '',
        'completed': '',
        }
        widgets = {
            'client': forms.Select(attrs={'class':'form-control', 'placeholder':'Client'}),
            'document_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Document Type' }),
            'bank': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bank'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Document Description'}),
            'document': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Add File:'}),
        }



class ClientGroupForm(forms.ModelForm):
    class Meta:
        model = ClientGroup
        fields = ['client_group']
        labels = {
        'client_group': '',

        }
        widgets = {
            'client_group': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Client Group' }),
        }

class EmployeeForm(forms.ModelForm):
    class meta:
        model = Employee
        fields = ['manager']
        labels = {
        'manager':'',
        }
        widgets = {
            'manager': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Manager'}),
        }

class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industrie
        fields = ['industry_type_drop']
        labels = {
        'industry_type_drop':'',
        }
        widgets = {
            'industry_type_drop': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Industry'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['client_name', 'c_name_1', 'c_num_1', 'c_email_1', 'c_name_2', 'c_num_2', 'c_email_2', 'c_name_3', 'c_num_3', 'c_email_3', 'c_name_4', 'c_num_4', 'c_email_4', 'c_name_5', 'c_num_5', 'c_email_5',  ]
        labels = {
            'client_name':'',
            'c_name_1':'',
            'c_num_1':'',
            'c_email_1':'',
            'c_name_2':'',
            'c_num_2':'',
            'c_email_2':'',
            'c_name_3':'',
            'c_num_3':'',
            'c_email_3':'',
            'c_name_4':'',
            'c_num_4':'',
            'c_email_4':'',
            'c_name_5':'',
            'c_num_5':'',
            'c_email_5':'',
        }
        widgets = {
            'client_name': forms.Select(attrs={'class':'form-control', 'placeholder':'Client'}),
            'c_name_1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Name'}),
            'c_num_1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'c_email_1': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Contact Email'}),
            'c_name_2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Name'}),
            'c_num_2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'c_email_2': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Contact Email'}),
            'c_name_3': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Name'}),
            'c_num_3': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'c_email_3': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Contact Email'}),
            'c_name_4': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Name'}),
            'c_num_4': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'c_email_4': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Contact Email'}),
            'c_name_5': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Name'}),
            'c_num_5': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'c_email_5': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Contact Email'}),
        }
