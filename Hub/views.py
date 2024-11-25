from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import redirect

# Home Page
def home(request):
    return render(request, 'home.html')

# About Us Page
def about(request):
    return render(request, 'about.html')

# Artist Page
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, 'artist_detail.html', {'artist': artist})

# Event Page
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

# Gallery Page
def gallery(request, category):
    gallery_images = Gallery.objects.filter(category=category)
    return render(request, 'gallery.html', {'gallery_images': gallery_images})

# Login & Signup views (simplified)
def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def artist_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        bio = request.POST['bio']
        image = request.FILES['image']
        Artist.objects.create(name=name, bio=bio, image=image)
        return redirect('home')
    return render(request, 'artist_create.html')

def artist_update(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == 'POST':
        artist.name = request.POST['name']
        artist.bio = request.POST['bio']
        artist.image = request.FILES['image']
        artist.save()
        return redirect('artist_detail', artist_id=artist.id)
    return render(request, 'artist_update.html', {'artist': artist})

def artist_delete(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    artist.delete()
    return redirect('home')
