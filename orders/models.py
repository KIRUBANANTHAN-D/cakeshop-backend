import uuid
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cake(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="cakes"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cakes/', blank=True, null=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    map_url = models.URLField(blank=True, null=True)
    open_time = models.CharField(max_length=20)
    close_time = models.CharField(max_length=20)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
        null=True,
        blank=True
    )

    order_no = models.CharField(max_length=20, unique=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    weight = models.FloatField()
    egg_type = models.CharField(max_length=20)
    delivery_type = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    total = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_no:
            self.order_no = "ORD" + uuid.uuid4().hex[:8].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_no