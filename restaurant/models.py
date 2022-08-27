from django.db import models

# Create your models here.
class dimsumItems(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.CharField(max_length = 5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Dim Sum"

class appetizerItems(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.CharField(max_length = 5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Appetizers"

class baoItems(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.CharField(max_length = 5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Baos"

class noodleSoupItems(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.CharField(max_length = 5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Noodle Soups"

class sushiItems(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    price = models.CharField(max_length = 5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sushi"

class dessertItems(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.CharField(max_length = 5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Desserts"

class drinkItems(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.CharField(max_length = 5)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Drinks"

class reservations(models.Model):
    title = models.CharField(max_length = 50)
    time = models.CharField(max_length = 50)
    date = models.CharField(max_length = 20)
    people = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Reservations"

class notification(models.Model):
    title = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    message = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Notifications"