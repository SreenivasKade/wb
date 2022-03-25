from django.contrib import admin
from .models import Move
# Register your models here.

class MoveAdmin(admin.ModelAdmin):
    list_display = ('id','movement', 'time', 'created_at')
    list_per_page = 20
admin.site.register(Move, MoveAdmin)
