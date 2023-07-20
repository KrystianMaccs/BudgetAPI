from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['category', 'amount', 'owner', 'date', 'created_at', 'updated_at']
    list_filter = ['category', 'date', 'created_at']
    search_fields = ['category', 'description', 'owner__username']
    list_per_page = 20

admin.site.register(Expense, ExpenseAdmin)

