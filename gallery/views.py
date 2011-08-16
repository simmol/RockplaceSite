# Django
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from gallery.picasa import simpleGallery

def index(requst):
  simple = simpleGallery()
  albums = simple.getAlbums()

  gallery = []
  for album in albums:

    photos = simple.getPhotos(album.gphoto_id.text)
    photo = {}
    try:
      photo['title'] = photos[0].title.text
      photo['src']   = photos[0].media.thumbnail[0].url
    except IndexError:
      pass

    album_info = {
      'title': album.title.text,
      'id': album.gphoto_id.text,
      'photos_numbers': album.numphotos.text,
      'album_photo': photo,
      'url': reverse('name-album', args=[album.gphoto_id.text])
    }

    if(photo):
      gallery.append(album_info)

  return render_to_response('gallery/index.html', {'gallery': gallery})

def album(request, album_id):
  gallery = simpleGallery()

  photos = gallery.getPhotos(album_id)
 
  album = []
  for photo in photos:
    photo_info = {
      'title': photo.title.text,
      'src': photo.media.thumbnail[2].url
    }
    album.append(photo_info)

  return render_to_response('gallery/album.html', {'album': album})
