from django.utils.timezone import now
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, TextField

from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

class Link(Model):
    value = CharField(max_length=25, blank=False, null=False)
    expires = DateTimeField(default=now)
    protected_data = TextField()
    user = ForeignKey(User, on_delete=CASCADE)
