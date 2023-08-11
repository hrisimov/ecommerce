from django.contrib import admin

from ecommerce.products.models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_on', 'created_on')
    prepopulated_fields = {'slug': ('name',)}


class ProductImageInLine(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category_name', 'updated_on', 'created_on')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (ProductImageInLine,)

    @staticmethod
    def category_name(obj):
        return obj.category.name


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'product_name', 'is_main', 'updated_on', 'created_on')
    list_editable = ('is_main',)

    @staticmethod
    def image_name(obj):
        return str(obj.image).split('/')[1]

    @staticmethod
    def product_name(obj):
        return obj.product.name
