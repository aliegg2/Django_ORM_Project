from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    SEX_CHOICES = [
        ("M","Male"),
        ("F", "Female"),
        ("O", "Other")
    ]
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    age = models.PositiveBigIntegerField(blank=True,null=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(choices=SEX_CHOICES, max_length=10)


    #def __str__(self):
     #   return self.username

class Post(models.Model):
    VISIBILITY_CHOICES = [
        ("public", "Public"),
        ("private", "Private")
    ]
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="user_posts")
    content = models.TextField()
    categories = models.CharField(max_length=100)
    visibility = models.CharField(max_length=20,choices=VISIBILITY_CHOICES,default="public")
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="post_image/",blank=True,null=True)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="item_images/", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="cart")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} in {self.cart.user.username}'s cart"


