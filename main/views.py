# main/views.py

from django.views.generic import TemplateView, ListView, DetailView
from .models import Service, Project, Employee, NewsArticle, SiteConfiguration

class SiteConfigurationMixin:
    """
    Her view'a SiteConfiguration nesnesini (genel site ayarları)
    otomatik olarak ekleyen bir mixin.
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Sitede sadece bir tane ayar nesnesi olacağı varsayımıyla ilkini alıyoruz.
        context['site_config'] = SiteConfiguration.objects.first()
        return context

class HomeView(SiteConfigurationMixin, TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Anasayfada göstermek üzere son eklenenleri alıyoruz.
        context['services'] = Service.objects.all()[:3]
        context['projects'] = Project.objects.all()[:3]
        context['news_articles'] = NewsArticle.objects.all()[:3]
        return context

class AboutUsView(SiteConfigurationMixin, TemplateView):
    template_name = 'main/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Model'deki Meta.ordering sayesinde çalışanlar zaten sıralı gelecektir.
        context['employees'] = Employee.objects.all()
        # Hakkımızda metinleri site_config içinde zaten mevcut.
        return context

# --- Hizmetler (Services) ---
class ServiceListView(SiteConfigurationMixin, ListView):
    model = Service
    template_name = 'main/service_list.html'
    context_object_name = 'services'

class ServiceDetailView(SiteConfigurationMixin, DetailView):
    model = Service
    template_name = 'main/service_detail.html'
    context_object_name = 'service'
    # URL'de slug kullanacağımızı belirtiyoruz.

# --- Projeler (Projects) ---
class ProjectListView(SiteConfigurationMixin, ListView):
    model = Project
    template_name = 'main/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(SiteConfigurationMixin, DetailView):
    model = Project
    template_name = 'main/project_detail.html'
    context_object_name = 'project'

# --- Haberler (News) ---
class NewsListView(SiteConfigurationMixin, ListView):
    model = NewsArticle
    template_name = 'main/news_list.html'
    context_object_name = 'news_articles'
    paginate_by = 6 # Sayfalama: Her sayfada 6 haber göster

class NewsDetailView(SiteConfigurationMixin, DetailView):
    model = NewsArticle
    template_name = 'main/news_detail.html'
    context_object_name = 'article'

# --- İletişim (Contact) ---
class ContactView(SiteConfigurationMixin, TemplateView):
    template_name = 'main/contact.html'
    # İletişim bilgileri site_config içinde zaten mevcut.