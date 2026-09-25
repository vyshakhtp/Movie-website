from django.contrib import admin
from .models import Category,Movies,Comment,Favourite

admin.site.register(Category)
admin.site.register(Movies)
admin.site.register(Comment)
admin.site.register(Favourite)
