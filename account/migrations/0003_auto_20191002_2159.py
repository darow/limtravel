# Generated by Django 2.2.3 on 2019-10-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190930_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='has_purchases',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='paid_for_partner',
            field=models.BooleanField(default=False),
        ),
    ]
