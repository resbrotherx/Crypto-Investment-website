# Generated by Django 3.2.8 on 2021-11-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crpyto', '0011_membership_payhistory_subscription_usermembership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwallet',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userwallet',
            name='date',
        ),
        migrations.RemoveField(
            model_name='userwallet',
            name='private_key',
        ),
        migrations.RemoveField(
            model_name='userwallet',
            name='public_key',
        ),
        migrations.AddField(
            model_name='userwallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='userwallet',
            name='bonus',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='userwallet',
            name='deposited',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='userwallet',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='userwallet',
            name='ref_bonus',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]