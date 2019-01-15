from django.db import models
from django.core.validators import MaxValueValidator
from random import randint
from django.utils import timezone

class Package(models.Model):
    RECEIVED = 'RE'
    DELIVERED = 'DE'
    PACKAGE_STATUS = (
        (RECEIVED, 'Received in office'),
        (DELIVERED, 'Delivered to student'),
    )
    order_id = models.CharField(max_length=35)
    roll_no = models.CharField(max_length=30)
    delivery_service = models.CharField(max_length=30)
    otp = models.IntegerField(default=randint(100000,999999))
    status = models.CharField(max_length=2,choices=PACKAGE_STATUS,default=RECEIVED)
    received_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    delivered_time = models.DateTimeField(null=True,blank=True)
    pile_no = models.IntegerField(blank=True,default=((timezone.now()).day % 7),validators=[MaxValueValidator(7)])

    def __str__(self):
        return self.roll_no    