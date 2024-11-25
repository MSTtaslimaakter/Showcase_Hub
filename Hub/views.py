from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import redirect

# Home Page
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def artist(request):
    return render(request, 'artist.html')

def event(request):
    return render(request, 'event.html')

def gallery(request):
    return render(request, 'gallery.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')



def artist_detail(request, artist_id):
    
    artist = get_object_or_404(Artist, id=artist_id)
    artists = Artist.objects.exclude(id=artist_id)
    return render(request, 'artist_showcase/artist_detail.html', {'artist': artist, 'artists': artists})


def gallery(request, category=None):
    if category:
        galleries = Gallery.objects.filter(category=category)
    else:
        galleries = Gallery.objects.all()
    
    return render(request, 'gallery.html', {'galleries': galleries, 'category': category})

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

def artist_s(request):
    artists=Artist.objects.all()
    context={
       'artists': artists,
    }
    return render (request,'artist_profile.html',context=context)
