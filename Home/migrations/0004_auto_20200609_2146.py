# Generated by Django 3.0.3 on 2020-06-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20200609_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancehistory',
            name='UserMobile',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='withdraws',
            name='UserMobile',
            field=models.CharField(max_length=50),
        ),
    ]
