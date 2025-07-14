# main/management/commands/populate_db.py

import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.utils import timezone
from faker import Faker
from main.models import Service, Project, Employee, NewsArticle, SiteConfiguration

# Türkçe ve İngilizce için Faker nesneleri
fake_tr = Faker('tr_TR')
fake_en = Faker('en_US')

class Command(BaseCommand):
    help = 'Populates the database with fake data for testing.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        # Mevcut verileri temizle
        Service.objects.all().delete()
        Project.objects.all().delete()
        Employee.objects.all().delete()
        NewsArticle.objects.all().delete()
        SiteConfiguration.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Old data deleted.'))

        # --- SiteConfiguration Oluştur ---
        self.stdout.write('Creating Site Configuration...')
        config = SiteConfiguration.objects.create(
            site_name="OneEye Kurumsal",
            about_us_title_tr="Biz Kimiz?",
            about_us_title_en="Who We Are",
            about_us_content_tr=fake_tr.paragraph(nb_sentences=10),
            about_us_content_en=fake_en.paragraph(nb_sentences=10),
            team_section_title_tr="Harika Ekibimizle Tanışın",
            team_section_title_en="Meet Our Awesome Team",
            contact_page_content_tr="Bizimle iletişime geçmek için aşağıdaki bilgileri kullanabilir veya formu doldurabilirsiniz.",
            contact_page_content_en="You can use the information below to contact us or fill out the form.",
            footer_text_tr=f"© {fake_tr.year()} OneEye. Tüm Hakları Saklıdır.",
            footer_text_en=f"© {fake_en.year()} OneEye. All Rights Reserved.",
            email=fake_en.company_email(),
            phone=fake_tr.phone_number(),
            address=fake_tr.address()
        )
        self.stdout.write(self.style.SUCCESS('Site Configuration created.'))

        # --- Hizmetleri (Services) Oluştur ---
        service_icons = ['fas fa-cogs', 'fas fa-chart-line', 'fas fa-bullhorn', 'fas fa-shield-alt', 'fas fa-code', 'fas fa-rocket']
        self.stdout.write(f'Creating {len(service_icons)} services...')
        for icon in service_icons:
            Service.objects.create(
                name_tr=fake_tr.catch_phrase(),
                name_en=fake_en.catch_phrase(),
                description_tr=fake_tr.sentence(nb_words=10),
                description_en=fake_en.sentence(nb_words=10),
                content_tr=fake_tr.paragraph(nb_sentences=15),
                content_en=fake_en.paragraph(nb_sentences=15),
                icon=icon
            )
        self.stdout.write(self.style.SUCCESS(f'{len(service_icons)} services created.'))

        # --- Projeleri (Projects) Oluştur ---
        self.stdout.write('Creating 4 projects...')
        for i in range(4):
            project = Project(
                name_tr=f"Proje {fake_tr.word().capitalize()}",
                name_en=f"Project {fake_en.word().capitalize()}",
                description_tr=fake_tr.sentence(nb_words=12),
                description_en=fake_en.sentence(nb_words=12),
                content_tr=fake_tr.text(max_nb_chars=2000),
                content_en=fake_en.text(max_nb_chars=2000),
            )
            # Placeholder resim indir ve kaydet
            img_url = 'https://picsum.photos/800/600'
            try:
                response = requests.get(img_url)
                if response.status_code == 200:
                    project.image.save(f'project_{i+1}.jpg', ContentFile(response.content), save=True)
                else:
                    project.save()
            except requests.exceptions.RequestException:
                project.save() # İnternet yoksa resimsiz kaydet
        self.stdout.write(self.style.SUCCESS('4 projects created.'))


        # --- Çalışanları (Employees) Oluştur ---
        self.stdout.write('Creating 8 employees...')
        for i in range(8):
            employee = Employee(
                full_name=fake_tr.name(),
                title_tr=fake_tr.job(),
                title_en=fake_en.job(),
                bio_tr=fake_tr.paragraph(nb_sentences=3),
                bio_en=fake_en.paragraph(nb_sentences=3),
                linkedin_url='https://linkedin.com/',
                order=i
            )
            img_url = 'https://picsum.photos/400/400'
            try:
                response = requests.get(img_url)
                if response.status_code == 200:
                    employee.photo.save(f'employee_{i+1}.jpg', ContentFile(response.content), save=True)
                else:
                    employee.save()
            except requests.exceptions.RequestException:
                employee.save()
        self.stdout.write(self.style.SUCCESS('8 employees created.'))

        # --- Haberleri (NewsArticles) Oluştur ---
        self.stdout.write('Creating 15 news articles...')
        for i in range(15):
            naive_date = fake_en.date_time_this_year()

            aware_date = timezone.make_aware(naive_date)

            article = NewsArticle(
                title_tr=fake_tr.sentence(nb_words=6),
                title_en=fake_en.sentence(nb_words=6),
                summary_tr=fake_tr.paragraph(nb_sentences=2),
                summary_en=fake_en.paragraph(nb_sentences=2),
                content_tr=fake_tr.text(max_nb_chars=3000),
                content_en=fake_en.text(max_nb_chars=3000),
                published_date=aware_date
            )
            img_url = 'https://picsum.photos/1200/800'
            try:
                response = requests.get(img_url)
                if response.status_code == 200:
                    article.image.save(f'news_{i+1}.jpg', ContentFile(response.content), save=True)
                else:
                    article.save()
            except requests.exceptions.RequestException:
                article.save()
        self.stdout.write(self.style.SUCCESS('15 news articles created.'))

        self.stdout.write(self.style.SUCCESS('------------------------------------'))
        self.stdout.write(self.style.SUCCESS('Database successfully populated!'))
        self.stdout.write(self.style.SUCCESS('------------------------------------'))