# Generated by Django 3.2 on 2021-07-15 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210715_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='client_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.client'),
            preserve_default=False,
        ),
    ]
