from django import forms
from .models import Client, File, ClientGroup

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'contact_name', 'contact_number', 'contact_email', 'client_type', 'industry_type',
                'project_manager', 'tax_id', 'bank_accounts', 'client_group', ]
        labels = {
        'client_name': '',
        'contact_name': '',
        'contact_number': '',
        'contact_email': '',
        'client_type': '',
        'industry_type': '',
        'project_manager': '',
        'tax_id': '',
        'bank_accounts': '',
        'client_group': '',
        }
        widgets = {
            'client_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Client Name'}),
            'contact_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Name' }),
            'contact_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact Number'}),
            'contact_email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Contact Email'}),
            'client_type': forms.Select(attrs={'class':'form-control'}),
            'industry_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Industry Type'}),
            'project_manager': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Project Manager'}),
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
