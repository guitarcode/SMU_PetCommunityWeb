from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Member, Profile

# admin에서 Meber 정보와 Profile 정보가 같이 보여지도록 함
class ProfileInline(admin.StackedInline):
    model = Profile
    con_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.register(Member, CustomUserAdmin)