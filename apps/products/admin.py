from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Brand, Color, Product, ProductImage, Review, Tag, Size, ProductSize, Contact, About, DetailReviewModel
from django.utils.html import mark_safe

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields={'slug':('name',)}
    search_fields=('id', 'name')
    mptt_indent_field = "name"
    list_display=('tree_actions', 'indented_title', 'display_icon', 'created_at', 'is_active', 'id')
    list_display_links=('indented_title', 'display_icon', 'id')
    readonly_fields=('id', 'display_icon')
    
    def display_icon(self, obj):
        return mark_safe('<img src="%s" width="50" />' % obj.icon.url)
    
    display_icon.allow_tags = True
    display_icon.short_description = 'Icon'


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields=('id', 'name')
    list_display=['name', 'display_icon', 'id', 'created_at']
    list_display_links=('name', 'id')
   
    readonly_fields=('id', 'display_icon')

    def display_icon(self, obj):
        return mark_safe('<img src="%s" width="100" height="100" />' % obj.icon.url)

    display_icon.allow_tags = True
    display_icon.short_description = 'Icon'


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display=('name', 'code', 'created_at', 'id', 'is_active')
    list_editable=('code', 'is_active')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=('name', 'created_at')
    list_display_links=('name', 'created_at')
    search_fields=('name', 'id')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display= ('name', 'created_at')
    list_display_links=('name', 'created_at')
    search_fields=('name', 'id')

class ProductImageInline(admin.StackedInline):
    readonly_fields=('get_image', 'updated_at')
    model = ProductImage
    extra = 1

class ProductSizeAdmin(admin.TabularInline):
    model = ProductSize
    extra=1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSizeAdmin, ProductImageInline]
    prepopulated_fields={'slug': ('title', )}
    list_display = ('title', 'percentage', 'brand', 'id', 'status', 'is_active')
    search_fields=('title', 'status', 'brand',)
    list_filter=['created_at', 'status', 'is_active']
    list_display_links=('title', 'brand', 'id')
    filter_horizontal = ('categories', 'tags', )
    list_editable = ('status', 'is_active')
    list_per_page = 25


@admin.register(Review)
class RateAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'product', 'created_at')
    list_display_links = ('user', 'rating', 'product', 'created_at')
    search_fields = ('product', 'id', 'user')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'email', 'phone', 'email', 'subject')
    list_display_links = ('firstname', 'email', 'phone', 'email', 'subject')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=('address', 'phone', 'facebook', 'youtube')
    list_display_links=('address', 'phone', 'facebook', 'youtube')


@admin.register(DetailReviewModel)
class DetailReviewModelAdmin(admin.ModelAdmin):
    list_display= ('name', 'email', 'website')
    list_display_links = ('name', 'email', 'website')
    



