# main/translation.py

from modeltranslation.translator import translator, TranslationOptions
from .models import Service, Project, Employee, NewsArticle, SiteConfiguration

class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'content')

class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'content')

class EmployeeTranslationOptions(TranslationOptions):
    fields = ('title', 'bio')

class NewsArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'content')

class SiteConfigurationTranslationOptions(TranslationOptions):
    fields = ('about_us_title', 'about_us_content', 'team_section_title', 'contact_page_content', 'footer_text')

# Modelleri ve çeviri seçeneklerini kaydet
translator.register(Service, ServiceTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(Employee, EmployeeTranslationOptions)
translator.register(NewsArticle, NewsArticleTranslationOptions)
translator.register(SiteConfiguration, SiteConfigurationTranslationOptions)