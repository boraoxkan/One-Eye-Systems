from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Service, Project, SiteConfiguration

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('name', 'icon', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(TranslationAdmin):
    list_display = ('site_title', 'careers_enabled')
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_title', 'site_description', 'about_us', 'contact_info')
        }),
        ('Features', {
            'fields': ('video_url', 'careers_enabled')
        }),
    )
