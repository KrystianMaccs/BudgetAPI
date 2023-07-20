from django.contrib import admin
from .models import Goal

class GoalAdmin(admin.ModelAdmin):
    list_display = ['goal', 'owner', 'completed']
    list_filter = ['completed', 'owner__username']
    search_fields = ['goal', 'owner__username']
    list_per_page = 20

admin.site.register(Goal, GoalAdmin)
