from django.contrib import admin
from .models import CustomUser, Post, Item, Cart, CartItem

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)

