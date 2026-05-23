from django.contrib import admin
from .models import RecipePhoto


class RecipePhotoAdmin(admin.ModelAdmin):
    """Admin interface for RecipePhoto model"""
    
    list_display = ['title', 'owner', 'uploaded_at', 'get_description_preview']
    list_filter = ['uploaded_at', 'owner']
    search_fields = ['title', 'description', 'owner__username']
    readonly_fields = ['uploaded_at', 'get_image_preview']
    
    fieldsets = (
        ('Photo Information', {
            'fields': ('title', 'description', 'image', 'get_image_preview')
        }),
        ('Ownership', {
            'fields': ('owner',),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('uploaded_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_description_preview(self, obj):
        """Display preview of description"""
        if obj.description:
            return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
        return '-'
    get_description_preview.short_description = 'Description'
    
    def get_image_preview(self, obj):
        """Display thumbnail of image in admin"""
        if obj.image:
            return f'<img src="{obj.image.url}" width="200" />'
        return 'No image'
    get_image_preview.allow_tags = True
    get_image_preview.short_description = 'Image Preview'
    
    def get_readonly_fields(self, request, obj=None):
        """Make owner readonly on existing photos (only change via forms)"""
        if obj:
            return self.readonly_fields + ['owner']
        return self.readonly_fields


# Register the model with custom admin interface
admin.site.register(RecipePhoto, RecipePhotoAdmin)