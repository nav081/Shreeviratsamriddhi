# Generated by Django 3.0.3 on 2020-06-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20200613_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='EPIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserMobile', models.CharField(max_length=50)),
                ('PINCount', models.IntegerField()),
                ('RequestDate', models.DateField()),
                ('Amount', models.CharField(blank=True, max_length=50, null=True)),
                ('TransactionID', models.CharField(blank=True, max_length=100, null=True)),
                ('To', models.CharField(max_length=50)),
                ('Screenshot', models.ImageField(blank=True, null=True, upload_to='UsersPhoto')),
                ('Status', models.CharField(max_length=50)),
            ],
        ),
    ]