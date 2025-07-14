# main/admin.py

from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from adminsortable2.admin import SortableAdminMixin

from .models import Service, Project, Employee, NewsArticle, SiteConfiguration

@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'icon')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(TabbedTranslationAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Employee)
class EmployeeAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    # Sürükle-bırak sıralaması ve çeviri sekmeleri bir arada
    list_display = ('full_name', 'title', 'order')
    list_editable = ('order',) # İsteğe bağlı: Sıralamayı manuel de değiştirebilmek için

@admin.register(NewsArticle)
class NewsArticleAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'published_date')
    list_filter = ('published_date',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(TabbedTranslationAdmin):
    # Bu modelden sadece bir tane olmasını sağlamak için admin panelinde ekleme butonunu gizleyebiliriz.
    def has_add_permission(self, request):
        # Eğer zaten bir ayar nesnesi varsa, yenisini eklemeye izin verme
        return SiteConfiguration.objects.count() == 0

    # Silme iznini de kaldıralım
    def has_delete_permission(self, request, obj=None):
        return False