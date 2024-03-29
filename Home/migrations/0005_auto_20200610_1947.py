# Generated by Django 3.0.3 on 2020-06-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20200609_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserMobile', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('RequestDate', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='KYCMsg',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='withdraws',
            name='Name',
            field=models.CharField(default='Navneet k Yadav', max_length=50),
            preserve_default=False,
        ),
    ]
