from django.contrib import admin
from django.contrib.auth import get_user_model

from rest_framework.authtoken.admin import TokenAdmin


TokenAdmin.raw_id_fields = ('user', )


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
