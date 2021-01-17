from django.db import models

"""Veritabanı Tablo modellerini burda oluşturduk"""
class SensorA(models.Model):
    temp = models.CharField(max_length=20)
    air = models.CharField(max_length=20)
    co = models.CharField(max_length=20)
    lpg = models.CharField(max_length=20)
    smoke = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)
