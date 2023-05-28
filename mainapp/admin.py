from django.contrib import admin
from .models import User, Content

admin.site.register(User)
admin.site.register(Content)
# class UserAdmin(admin.ModelAdmin):
#     list_display=["id", "first_name"]