# Generated by Django 4.0.6 on 2022-08-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='pincode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]