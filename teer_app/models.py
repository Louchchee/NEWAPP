from django.db import models
from django.contrib.auth.models import User



class Counters(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    counter_circle = models.CharField(max_length=40, blank=False, null=False)
    liscense = models.IntegerField(primary_key=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    select_number = models.IntegerField()
    counter = models.ForeignKey(Counters, on_delete=models.CASCADE)
    price = models.IntegerField(blank=False, null=False)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Result(models.Model):
    counter = models.ForeignKey(Counters, on_delete=models.CASCADE)
    result = models.IntegerField(primary_key=True,blank=False, null=False)
    result_declare_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.counter.counter_circle

class Winners(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wining_number =  models.ForeignKey(Result,on_delete=models.CASCADE, blank=False, null=False)
    booking_code = models.ForeignKey(Booking, on_delete=models.CASCADE) 
    