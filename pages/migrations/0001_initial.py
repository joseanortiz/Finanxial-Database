# Generated by Django 3.2 on 2021-07-15 20:11

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('contact_email', models.EmailField(max_length=200)),
                ('contact_name_1', models.CharField(blank=True, max_length=200)),
                ('contact_number_1', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('contact_email_1', models.EmailField(blank=True, max_length=200)),
                ('client_type', models.CharField(choices=[('Data Entry', 'Data Entry'), ('Reconcile and Review', 'Reconcile and Review'), ('Review', 'Review')], max_length=200)),
                ('industry_type', models.CharField(blank=True, max_length=200)),
                ('project_manager', models.CharField(blank=True, max_length=200)),
                ('tax_id', models.CharField(max_length=200)),
                ('bank_accounts', models.CharField(blank=True, max_length=200)),
                ('client_group', models.CharField(max_length=200)),
                ('accounting', models.BooleanField(default=False)),
                ('taxes', models.BooleanField(default=False)),
                ('audits', models.BooleanField(default=False)),
                ('tax_consulting', models.BooleanField(default=False)),
                ('consulting', models.BooleanField(default=False)),
                ('investment', models.BooleanField(default=False)),
                ('planning', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ClientGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_group', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Industrie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_type_drop', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(blank=True, max_length=200)),
                ('bank', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('document', models.FileField(blank=True, upload_to='files/')),
                ('completed', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.client')),
            ],
        ),
    ]
