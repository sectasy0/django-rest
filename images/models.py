from django.contrib.auth.models import User

from uuid import uuid4
from os.path import join
from django.db.models.base import Model

from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import BooleanField, CharField, IntegerField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, OneToOneField


class Plan(Model):
    plan_name = CharField(max_length=100)
    
    acces_original = BooleanField(default=False)
    expiration_links = BooleanField(default=False)

    def __str__(self):
        return f"{self.plan_name}"


class ThumbnailSize(Model):
    h = IntegerField(default=200)
    w = IntegerField(default=200)

    plan = ForeignKey(Plan, on_delete=DO_NOTHING)

    def __str__(self):
        return f"{self.h}x{self.w}"


def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = f"{instance.user}_{(uuid4().hex[:12].upper())}.{ext}"
        return join('uploads/', filename)


class Image(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    image = ImageField(upload_to=get_file_path)
    thumbnail200 = ImageField(blank=True, null=True, upload_to=get_file_path)
    thumbnail400 = ImageField(blank=True, null=True, upload_to=get_file_path)


    def __str__(self):
        return f"{self.user}, {self.image}"
        

class UserPlan(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    plan = OneToOneField(Plan, on_delete=CASCADE)

    def __str__(self):
        return f"{self.user}, {self.plan}"
