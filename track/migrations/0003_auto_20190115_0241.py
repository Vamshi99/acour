# Generated by Django 2.1.5 on 2019-01-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20190115_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='otp',
            field=models.IntegerField(default=674017),
        ),
        migrations.AlterField(
            model_name='package',
            name='received_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
