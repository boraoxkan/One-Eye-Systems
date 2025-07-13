# One Eye Systems - Kurumsal Web Sitesi

Django ve Bootstrap 5 kullanarak geliştirilen modern ve dinamik kurumsal web sitesi. Referans alınan site: [oneeyesystems.com](https://www.oneeyesystems.com/)

## 🌟 Özellikler

- **Tamamen Yönetilebilir İçerik**: Tüm metin, resim ve içerik blokları admin panelinden yönetilebilir
- **Modern Dark Theme**: Referans siteye uygun koyu tema ve cyan/turkuaz renk paleti
- **Dinamik Hizmetler**: Font Awesome ikonları ile hizmetler admin panelinden yönetilebilir
- **Proje Portföyü**: Gerçekleştirilen projelerin showcase'i
- **Kariyer Bölümü**: CV gönderimleri için e-posta entegrasyonu
- **Responsive Tasarım**: Tüm cihazlarda mükemmel görünüm
- **Smooth Scrolling**: Sayfa içi navigasyon
- **Sosyal Medya Entegrasyonu**: LinkedIn, Twitter, Instagram linkleri

## 🚀 Kurulum

### Gereksinimler

- Python 3.8+
- Django 5.2+
- Pillow (resim işleme)

### Kurulum Adımları

1. **Projeyi klonlayın:**
   ```bash
   git clone <repository-url>
   cd oneeye_website
   ```

2. **Virtual environment oluşturun:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # veya
   venv\Scripts\activate  # Windows
   ```

3. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Veritabanı migration'larını uygulayın:**
   ```bash
   python manage.py migrate
   ```

5. **Superuser oluşturun:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Sunucuyu çalıştırın:**
   ```bash
   python manage.py runserver
   ```

## 📁 Proje Yapısı

```
oneeye_website/
├── main/                    # Ana Django uygulaması
│   ├── models.py           # Service, Project, SiteConfiguration modelleri
│   ├── views.py            # Ana sayfa, hizmet ve proje detay görünümleri
│   ├── admin.py            # Özelleştirilmiş admin paneli
│   └── urls.py             # URL yapılandırması
├── templates/              # HTML şablonları
│   ├── base.html           # Temel şablon (Font Awesome, modern tasarım)
│   └── main/
│       ├── home.html       # Ana sayfa (Hero, About, Services, Projects, Career, Contact)
│       ├── service_detail.html  # Hizmet detay sayfası
│       └── project_detail.html  # Proje detay sayfası
├── static/                 # Statik dosyalar
├── media/                  # Yüklenen dosyalar
│   ├── services/           # Hizmet görselleri
│   ├── projects/           # Proje görselleri
│   ├── site_images/        # Site görselleri
│   └── site_videos/        # Site videoları
├── oneeye_website/         # Proje ayarları
└── requirements.txt        # Python paketleri
```

## 🎯 Kullanım

### Admin Paneli

1. **Erişim**: `http://localhost:8000/admin/`
2. **Giriş**: Oluşturduğunuz superuser bilgileri ile giriş yapın

### İçerik Yönetimi

#### Site Konfigürasyonu
- **Hero Bölümü**: Ana sayfa başlığı, alt başlığı ve arkaplan videosu
- **Hakkımızda**: Başlık, içerik ve görsel
- **Kariyer**: Başlık, içerik ve CV e-posta adresi
- **İletişim**: E-posta, telefon, adres bilgileri
- **Sosyal Medya**: LinkedIn, Twitter, Instagram URL'leri
- **Footer**: Açıklama metni

#### Hizmet Yönetimi
- **Font Awesome İkonları**: Hizmetler için ikon class'ları (örn: `fas fa-brain`)
- **Hizmet Detayları**: Başlık, kısa açıklama, detaylı içerik
- **Sıralama**: Hizmetlerin ana sayfada görünüm sırası
- **Aktif/Pasif**: Hizmetleri yayından kaldırma

#### Proje Yönetimi
- **Proje Portföyü**: Gerçekleştirilen projelerin showcase'i
- **Proje Görselleri**: Her proje için kapak resmi
- **Proje Detayları**: Kısa açıklama ve detaylı içerik
- **Sıralama**: Projelerin ana sayfada görünüm sırası

### Sayfa Yapısı

#### Ana Sayfa (`/`)
- **Hero Bölümü**: Video arkaplan ile etkileyici açılış
- **Hakkımızda**: Şirket bilgileri ve görsel
- **Hizmetler**: Font Awesome ikonları ile hizmet kartları
- **Projeler**: Proje portföyü showcase'i
- **Kariyer**: CV gönderim bölümü
- **İletişim**: İletişim bilgileri ve linkler

#### Hizmet Detay (`/services/<slug>/`)
- **Hizmet Detayları**: Tam açıklama ve ikon
- **İletişim Kartı**: Hızlı iletişim linkleri
- **Diğer Hizmetler**: İlgili hizmetler

#### Proje Detay (`/projects/<slug>/`)
- **Proje Detayları**: Tam açıklama ve görseller
- **İletişim Kartı**: Hızlı iletişim linkleri
- **Diğer Projeler**: İlgili projeler

## 🛠️ Teknik Detaylar

### Kullanılan Teknolojiler

- **Backend**: Django 5.2
- **Frontend**: Bootstrap 5.3 + Font Awesome 6.5
- **Veritabanı**: SQLite (geliştirme), PostgreSQL (prodüksiyon önerilir)
- **Typography**: Google Fonts - Poppins
- **Icons**: Font Awesome 6.5
- **Form Yönetimi**: Django Crispy Forms

### Tasarım Özellikleri

- **Renk Paleti**: Koyu tema (#0a0a0a, #1a1a1a) + Cyan vurgu (#00d4ff)
- **Typography**: Poppins font ailesi
- **Responsive**: Bootstrap 5 grid sistemi
- **Animations**: Smooth transitions ve hover effects
- **Navbar**: Transparan başlangıç, scroll'da opak

### Modeller

#### Service (Hizmet)
```python
- title: Hizmet başlığı
- icon_class: Font Awesome icon class
- short_description: Kısa açıklama
- detailed_content: Detaylı içerik
- slug: URL slug'ı
- is_active: Aktif/pasif durumu
- order: Sıralama
- cover_image: Kapak resmi (opsiyonel)
```

#### Project (Proje)
```python
- title: Proje başlığı
- cover_image: Kapak resmi
- short_description: Kısa açıklama
- detailed_content: Detaylı içerik
- slug: URL slug'ı
- is_active: Aktif/pasif durumu
- order: Sıralama
```

#### SiteConfiguration (Site Yapılandırması)
```python
# Hero Bölümü
- hero_title: Ana başlık
- hero_subtitle: Alt başlık
- hero_video: Arkaplan videosu

# Hakkımızda
- about_us_title: Hakkımızda başlığı
- about_us_content: Hakkımızda içeriği
- about_us_image: Hakkımızda görseli

# Kariyer
- career_title: Kariyer başlığı
- career_content: Kariyer içeriği
- career_cv_email: CV e-posta adresi

# İletişim
- contact_email: İletişim e-postası
- phone_number: Telefon numarası
- address: Adres

# Sosyal Medya
- linkedin_url: LinkedIn URL
- twitter_url: Twitter URL
- instagram_url: Instagram URL

# Footer
- footer_description: Footer açıklaması
```

## 📄 Örnek Veriler

Proje ile birlikte aşağıdaki örnek veriler otomatik olarak oluşturulmuştur:

### Hizmetler:
- Yapay Zeka Çözümleri (`fas fa-brain`)
- Web Geliştirme (`fas fa-code`)
- Mobil Uygulama (`fas fa-mobile-alt`)
- Bulut Çözümleri (`fas fa-cloud`)
- Veri Analizi (`fas fa-chart-line`)
- Siber Güvenlik (`fas fa-shield-alt`)

### Projeler:
- E-Ticaret Platformu
- Fintech Mobil Uygulaması
- IoT Akıllı Şehir Sistemi
- Sağlık Yönetim Sistemi

## 🎨 Özelleştirme

### Renk Paleti Değiştirme

`templates/base.html` dosyasındaki CSS değişkenlerini düzenleyin:

```css
:root {
    --primary-color: #00d4ff;
    --primary-dark: #0095cc;
    --bg-dark: #0a0a0a;
    --bg-light: #1a1a1a;
}
```

### Yeni Hizmet İkonu Ekleme

1. Admin paneline girin
2. Hizmetler bölümüne gidin
3. İkon Class alanına Font Awesome class'ını girin (örn: `fas fa-rocket`)

### Sosyal Medya Hesapları

Admin panelinde Site Konfigürasyonu bölümünden sosyal medya URL'lerini güncelleyin.

## 🔧 Troubleshooting

### Yaygın Sorunlar

1. **Font Awesome ikonları görünmüyor**:
   - CDN bağlantısını kontrol edin
   - İnternet bağlantınızı doğrulayın

2. **Videolar oynatılmıyor**:
   - Video formatının MP4 olduğundan emin olun
   - Dosya boyutunu kontrol edin

3. **Responsive tasarım bozuk**:
   - Bootstrap CDN bağlantısını kontrol edin
   - Browser cache'ini temizleyin

### Prodüksiyon Notları

- `DEBUG = False` yapın
- `ALLOWED_HOSTS` ayarını yapın
- PostgreSQL veya MySQL kullanın
- Statik dosyaları collect edin
- HTTPS sertifikası ekleyin
- Media dosyaları için CDN kullanın

## 📞 İletişim

- **Website**: [oneeyesystems.com](http://oneeyesystems.com)
- **Email**: info@oneeyesystems.com
- **Telefon**: +90 212 123 45 67

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. 