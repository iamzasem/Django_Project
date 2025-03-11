from django.urls import path # type: ignore
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery_view, name='gallery'),  # Changed to gallery_view
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('seo/', views.seo, name='seo'),
    path('thumbnails/', views.thumbnails, name='thumbnails'),
    path('digitalmarketing/', views.digitalmarketing, name='digitalmarketing'),
    path('search/', views.search, name='search'),
    path('myadmin/', views.custom_admin, name='custom_admin'),
]