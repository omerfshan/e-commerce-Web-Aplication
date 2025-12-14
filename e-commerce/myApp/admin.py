from django.contrib import admin
from .models import Product,Category,Supplier,Address

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","price","isActivate","slug","selectedCategories",)
    list_display_links=("name","price",)
    prepopulated_fields={"slug":("name",)}
    list_filter=("price","category",)
    list_editable=("isActivate",)
    search_fields=("name","description")

    def selectedCategories(self,obj):
      html=""
      
      for category in obj.category.all():
       html += category.name + " "

      return html
    

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Address)