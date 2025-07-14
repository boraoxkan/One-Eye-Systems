# main/models.py

from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Hizmet Adı")
    description = models.TextField(verbose_name="Kısa Açıklama (Anasayfa)")
    content = models.TextField(verbose_name="Detaylı İçerik (Hizmet Detay Sayfası)")
    icon = models.CharField(max_length=100, help_text="Örn: 'fas fa-cogs' (Font Awesome ikon sınıfı)", verbose_name="İkon Sınıfı")
    slug = models.SlugField(unique=True, max_length=220, editable=False, verbose_name="Slug")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetler"

class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="Proje Adı")
    description = models.TextField(verbose_name="Kısa Açıklama")
    content = models.TextField(verbose_name="Detaylı İçerik")
    image = models.ImageField(upload_to='projects/', verbose_name="Proje Görseli")
    slug = models.SlugField(unique=True, max_length=220, editable=False, verbose_name="Slug")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"

class Employee(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Tam Adı")
    title = models.CharField(max_length=100, verbose_name="Unvan")
    photo = models.ImageField(upload_to='team/', verbose_name="Fotoğraf")
    bio = models.TextField(blank=True, null=True, verbose_name="Biyografi")
    linkedin_url = models.URLField(blank=True, null=True, verbose_name="LinkedIn Profili")
    order = models.PositiveIntegerField(default=0, help_text="Sitedeki sıralamayı belirler (küçükten büyüğe).", verbose_name="Sıralama")

    def __str__(self):
        return f"{self.full_name} ({self.title})"

    class Meta:
        ordering = ['order']
        verbose_name = "Ekip Üyesi"
        verbose_name_plural = "Ekip Üyeleri"

class NewsArticle(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlık")
    slug = models.SlugField(unique=True, max_length=270, editable=False, verbose_name="Slug")
    image = models.ImageField(upload_to='news/', verbose_name="Görsel")
    summary = models.TextField(verbose_name="Özet")
    content = models.TextField(verbose_name="İçerik")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Yayınlanma Tarihi")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Haber/Makale"
        verbose_name_plural = "Haberler/Makaleler"


# Bu modelden sadece 1 tane oluşturulmalıdır.
class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=100, default="OneEye", verbose_name="Site Adı")
    about_us_title = models.CharField(max_length=200, verbose_name="Hakkımızda Başlığı")
    about_us_content = models.TextField(verbose_name="Hakkımızda İçeriği")
    team_section_title = models.CharField(max_length=200, default="Ekibimizle Tanışın", verbose_name="Ekip Bölümü Başlığı")
    contact_page_content = models.TextField(verbose_name="İletişim Sayfası İçeriği")
    footer_text = models.CharField(max_length=255, verbose_name="Footer Metni")
    email = models.EmailField(verbose_name="İletişim E-posta")
    phone = models.CharField(max_length=20, verbose_name="İletişim Telefon")
    address = models.TextField(verbose_name="Adres")

    def __str__(self):
        return f"{self.site_name} Ayarları"

    class Meta:
        verbose_name = "Site Genel Ayarı"
        verbose_name_plural = "Site Genel Ayarları"