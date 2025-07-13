# populate_slugs.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oneeye_website.settings')
django.setup()

from main.models import Service, Project
from django.utils.text import slugify

def populate_slugs(model, name_field='name'):
    for obj in model.objects.all():
        if not obj.slug or obj.slug.strip() == '':
            base = slugify(getattr(obj, name_field)) or model.__name__.lower()
            slug = base
            i = 1
            while model.objects.filter(slug=slug).exclude(id=obj.id).exists():
                slug = f"{base}-{i}"
                i += 1
            obj.slug = slug
            obj.save()
            print(f"{model.__name__} #{obj.id} için slug oluşturuldu: {slug}")

if __name__ == "__main__":
    populate_slugs(Service)
    populate_slugs(Project)
    print("Tüm slug alanları dolduruldu.")