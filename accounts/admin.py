from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.

UserAdmin.fieldsets[1][1]['fields'] = (
                        'first_name',
                        'last_name',
                        'email',
                        'phone_number',
                        'is_author',
)
admin.site.register(User,UserAdmin)