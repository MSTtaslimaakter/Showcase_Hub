

from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='artist_images/')

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='event_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('paintings', 'Paintings'),
        ('illustrations', 'Illustrations'),
        ('photography', 'Photography'),
        ('abstract_art', 'Abstract Art'),
        ('handcraft', 'Handcraft'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='gallery_images/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



