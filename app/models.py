from django.db import models
from django.contrib.auth.models import User
import datetime
from PIL import Image as Img
import hashlib
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.


class Groups(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=120,null=True)
    def __unicode__(self):
        return self.key

class Assignment(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField()
    view_count = models.IntegerField(default=0)
    upload_timestamp = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Groups)
    owner = models.ForeignKey(User)
    image_count = models.IntegerField(default=0)

class Images(models.Model):
    image = models.ImageField(upload_to='user_content')
    position = models.IntegerField()
    assignment = models.ForeignKey(Assignment)

    def save(self, *args, **kwargs):
        if self.image:
            img = Img.open(StringIO.StringIO(self.image.read()))
            img.thumbnail((self.image.width/1.5,self.image.height/1.5), Img.ANTIALIAS)
            date_time_hash = hashlib.md5(str(datetime.datetime.now())).hexdigest()
            output = StringIO.StringIO()
            img.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.image= InMemoryUploadedFile(output,'ImageField', "%s.jpg" %date_time_hash, 'image/jpeg', output.len, None)
        super(Images, self).save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    subscription = models.ManyToManyField(Groups)

