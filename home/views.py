from django.shortcuts import render, HttpResponse, redirect  # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.conf import settings # type: ignore
from .models import AlbumCategory, Photo
from django.http import JsonResponse # type: ignore
from django.core.paginator import Paginator # type: ignore
import os
from django.core.mail import send_mail # type: ignore

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):  # Note: Duplicated in URLs
    return render(request, 'gallery.html')

def search(request):
    query = request.GET.get('query', '')
    context = {'query': query}
    return render(request, 'search.html', context)

def seo(request):
    return render(request, 'seo.html')

def thumbnails(request):
    return render(request, 'thumbnails.html')

def digitalmarketing(request):
    return render(request, 'digitalmarketing.html')

def services(request):
    return render(request, 'services.html')

def gallery_page(request):
    albums = AlbumCategory.objects.prefetch_related('photos').all()
    context = {'albums': albums}
    return render(request, 'gallery.html', context)

def about_page(request):
    try:
        friends_album = AlbumCategory.objects.get(name='Friends')
        friends_photos = Photo.objects.filter(album=friends_album)
    except AlbumCategory.DoesNotExist:
        friends_photos = []
    
    try:
        projects_album = AlbumCategory.objects.get(name='Projects')
        project_photos = Photo.objects.filter(album=projects_album)
    except AlbumCategory.DoesNotExist:
        project_photos = []
    
    context = {
        'friends_photos': friends_photos,
        'project_photos': project_photos,
    }
    return render(request, 'about.html', context)

@login_required
def custom_admin(request):
    albums = AlbumCategory.objects.all()
    total_photos = Photo.objects.count()
    paginator = Paginator(albums, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'albums': page_obj,
        'total_photos': total_photos,
    }

    if request.method == 'POST':
        if 'add_album' in request.POST:
            name = request.POST.get('album_name')
            cover_image = request.FILES.get('cover_image')
            if name and cover_image:
                AlbumCategory.objects.create(name=name, cover_image=cover_image)
                return redirect('custom_admin')

        elif 'add_photo' in request.POST:
            album_id = request.POST.get('album')
            images = request.FILES.getlist('photo_image')
            if album_id and images:
                album = AlbumCategory.objects.get(id=album_id)
                for image in images:
                    title = request.POST.get('photo_title', f"Photo {image.name}")
                    Photo.objects.create(album=album, title=title, image=image)
                return redirect('custom_admin')

        elif 'delete_photo' in request.POST:
            photo_id = request.POST.get('photo_id')
            try:
                photo = Photo.objects.get(id=photo_id)
                photo.image.delete()
                photo.delete()
                return JsonResponse({'success': True})
            except Photo.DoesNotExist:
                return JsonResponse({'success': False}, status=404)

    return render(request, 'myadmin.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')


    if os.path.exists(gallery_path):
        for album_name in os.listdir(gallery_path):
            album_folder = os.path.join(gallery_path, album_name)
            if os.path.isdir(album_folder):
                photo_files = [
                    f for f in os.listdir(album_folder)
                    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
                ]
                if photo_files:
                    photos = [f'gallery/{album_name}/{file}' for file in photo_files]
                    albums.append({
                        'id': album_name,
                        'name': album_name.capitalize(),
                        'cover_image': photos[0],
                        'photos': photos,
                    })
    
    context = {'albums': albums}
    return render(request, 'gallery.html', context)

# Note: This appears again but with a different implementation
def gallery(request):
    albums = AlbumCategory.objects.all()  # Fixed from "Album" to "AlbumCategory"
    return render(request, 'gallery.html', {'albums': albums})

def gallery_view(request):
    albums = []
    gallery_path = os.path.join(settings.STATICFILES_DIRS[0], 'gallery')
    
    if os.path.exists(gallery_path):
        for album_name in os.listdir(gallery_path):
            album_folder = os.path.join(gallery_path, album_name)
            if os.path.isdir(album_folder):
                photo_files = [f for f in os.listdir(album_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
                if photo_files:
                    photos = [f'gallery/{album_name}/{file}' for file in photo_files]
                    albums.append({
                        'name': album_name.capitalize(),
                        'cover_image': photos[0],
                        'photos': photos
                    })
    
    return render(request, 'gallery.html', {'albums': albums})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email
        send_mail(
            subject=f"New Contact Form Message from {first_name}",
            message=f"From: {email}\n\nMessage: {message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['iamzasemworks@gmail.com'],  # Your email
            fail_silently=False,
        )
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def contact(request):
    whatsapp_number = "9779845996160"
    whatsapp_message = "Hi Zasem, I want to chat about a project!"
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={whatsapp_message.replace(' ', '%20')}"
    return render(request, 'contact.html', {'whatsapp_url': whatsapp_url})