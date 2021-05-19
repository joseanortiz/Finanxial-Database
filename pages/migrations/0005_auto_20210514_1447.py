# Generated by Django 3.2 on 2021-05-14 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_file_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_group',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='client_type',
            field=models.CharField(choices=[('Data Entry', 'Data Entry'), ('Reconcile and Review', 'Reconcile and Review'), ('Review', 'Review')], max_length=200),
        ),
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]