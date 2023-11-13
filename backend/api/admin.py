from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username',)
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('username', 'phone', 'dept', 'district')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('room_num', 'username', 'is_paid')
