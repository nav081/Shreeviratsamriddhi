# Generated by Django 3.0.7 on 2020-07-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_users_numberofaccounts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='Perdaycost',
            new_name='TotaldaysLeft1',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='TotaldaysLeft',
            new_name='TotaldaysLeft10',
        ),
        migrations.AddField(
            model_name='users',
            name='TotaldaysLeft11',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='TotaldaysLeft12',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='TotaldaysLeft2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='TotaldaysLeft3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='TotaldaysLeft4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='TotaldaysLeft5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='TotaldaysLeft6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='TotaldaysLeft7',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='TotaldaysLeft8',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
