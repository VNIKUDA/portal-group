from django.contrib import admin
from account.models import Profile, User

# Register your models here.
admin.site.register(Profile)
admin.site.register(User)