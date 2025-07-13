from django.shortcuts import render, get_object_or_404
from .models import Service, Project, SiteConfiguration


def home_view(request):
    """
    Ana sayfa görünümü
    """
    # Site konfigürasyonu, aktif hizmetleri ve aktif projeleri getir
    site_config = SiteConfiguration.objects.first()
    services = Service.objects.all()
    projects = Project.objects.all()
    
    context = {
        'config': site_config,
        'services': services,
        'projects': projects,
        'page_title': 'Ana Sayfa'
    }
    
    return render(request, 'main/home.html', context)


def service_detail_view(request, slug):
    """
    Hizmet detay sayfası görünümü
    """
    service = get_object_or_404(Service, slug=slug, is_active=True)
    site_config = SiteConfiguration.load()
    # Diğer hizmetleri de göndermek için
    services = Service.objects.filter(is_active=True).order_by('order', 'title')
    
    context = {
        'service': service,
        'site_config': site_config,
        'services': services,
        'page_title': service.title
    }
    
    return render(request, 'main/service_detail.html', context)


def project_detail_view(request, slug):
    """
    Proje detay sayfası görünümü
    """
    project = get_object_or_404(Project, slug=slug, is_active=True)
    site_config = SiteConfiguration.load()
    # Diğer projeleri de göndermek için
    projects = Project.objects.filter(is_active=True).order_by('order', 'title')
    
    context = {
        'project': project,
        'site_config': site_config,
        'projects': projects,
        'page_title': project.title
    }
    
    return render(request, 'main/project_detail.html', context)
