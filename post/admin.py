from django.contrib import admin
from post.models import Product, Category, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'created_at']
    list_editable = ['rate']
    list_filter = ['categories', 'created_at']
    list_per_page = 7
    search_fields = ['title', 'content', 'categories_title']

    def has_add_permission(self, request):
        return True

admin.site.register(Category)
admin.site.register(Comment)

