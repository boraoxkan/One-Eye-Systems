from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Service(models.Model):
    name = models.CharField(max_length=200, default='New Service')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    description = models.TextField(default='')
    content = models.TextField(default='')
    icon = models.CharField(max_length=50, default='fa-solid fa-star')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200, default='New Project')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    description = models.TextField(default='')
    content = models.TextField(default='')
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SiteConfiguration(models.Model):
    site_title = models.CharField(max_length=200, default='One Eye Systems')
    site_description = models.TextField(default='')
    about_us = models.TextField(default='')
    contact_info = models.TextField(default='')
    video_url = models.URLField(blank=True, null=True)
    careers_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'
