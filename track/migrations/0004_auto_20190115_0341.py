# Generated by Django 2.1.5 on 2019-01-14 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_auto_20190115_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='otp',
            field=models.IntegerField(default=732187),
        ),
    ]