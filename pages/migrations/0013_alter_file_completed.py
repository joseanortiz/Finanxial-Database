# Generated by Django 3.2 on 2021-05-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_file_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
