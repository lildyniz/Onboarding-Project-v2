from django.db import models


class Business(models.Model):
    business_type = models.CharField(max_length=100)

    def __str__(self):
        return self.business_type


class Direction(models.Model):
    direction = models.CharField(max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='Directions')

    def __str__(self):
        return self.direction
    

class Region(models.Model):
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.region


class City(models.Model):
    city = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.city


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='Users')
    business_direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='Users')
    previous_platform = models.CharField(max_length=100, blank=True, null=True) 

    def __str__(self):
        return self.name