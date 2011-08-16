# GData
import gdata.photos.service
import gdata.media
import gdata.geo

# Django
from django.conf import settings

class simpleGallery:
  """ Simple wraper of google picasa API
  """
  gd_client = None
  __authenticated = None

  def __init__(self):
    self.gd_client = gdata.photos.service.PhotosService()
    self.__connect()

  def __call__(self):
    return self

  def __connect(self, username =None, password =None, source =None ):
    if self.__authenticated is not None:
      return self.gd_client

    try:
      client = settings.GCLIENT
      self.gd_client.email     = username if username else client['email']
      self.gd_client.password  = password if password else client['password']
      self.gd_client.source    = source   if source   else client['source']

      self.__authenticated == self.gd_client.ProgrammaticLogin()

      return self.gd_client
    except AttributeError:
      return False

  def getClient(self):
    return self.gd_client

  def getAlbums(self):
    return self.gd_client.GetUserFeed().entry

  def getPhotos(self, album_id):
    photos = self.gd_client.GetFeed(
      '/data/feed/api/user/%s/albumid/%s?kind=photo' %
        ('default', album_id))

    return photos.entry


  def getPhoto(self, photo_id):
    raise NotImplemented
