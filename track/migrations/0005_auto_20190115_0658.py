# Generated by Django 2.1.5 on 2019-01-15 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0004_auto_20190115_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='delivered_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('RE', 'Received in office'), ('DE', 'Delivered to student')], default='RE', max_length=2),
        ),
        migrations.AlterField(
            model_name='package',
            name='otp',
            field=models.IntegerField(default=351663),
        ),
    ]
