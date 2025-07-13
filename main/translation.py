from modeltranslation.translator import register, TranslationOptions
from .models import Service, Project, SiteConfiguration

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'content')

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'content')

@register(SiteConfiguration)
class SiteConfigurationTranslationOptions(TranslationOptions):
    fields = ('site_title', 'site_description', 'about_us', 'contact_info') 