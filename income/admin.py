from django.contrib import admin
from .models import Income

class IncomeAdmin(admin.ModelAdmin):
    list_display = ['source', 'amount', 'owner', 'date', 'created_at', 'updated_at']
    list_filter = ['source', 'date', 'created_at']
    search_fields = ['source', 'description', 'owner__username']
    list_per_page = 20

admin.site.register(Income, IncomeAdmin)
