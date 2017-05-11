from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Article)
admin.site.register(models.Person)
admin.site.register(models.Group)
admin.site.register(models.Membership)
admin.site.register(models.Topping)
admin.site.register(models.Pizza)
admin.site.register(models.Place)
admin.site.register(models.Restaurant)


admin.site.register(models.MyPlace)
admin.site.register(models.Student)

