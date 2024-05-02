from django.db import models


class Business(models.Model):
    class BusinessTypes(models.TextChoices):
        Catering = 'Общепит'
        Retail = 'Ритейл'
        Tourism = 'Туризм'

    business_type = models.CharField(max_length=8, choices=BusinessTypes.choices)

    def __str__(self):
        return self.business_type

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='Users')

    def __str__(self):
        return self.name

class Direction(models.Model):
    name = models.CharField(max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='Directions')

    def __str__(self):
        return self.name
