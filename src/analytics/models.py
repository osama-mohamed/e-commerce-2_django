from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.sessions.models import Session
from django .db.models.signals import pre_save, post_save

from accounts.signals import user_logged_in
from .signals import object_viewed_signal
from .utils import get_client_ip

# Create your models here.

User = settings.AUTH_USER_MODEL


class ObjectViewed(models.Model):
  user            = models.ForeignKey(User, blank=True, null=True)
  content_type    = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
  object_id       = models.PositiveIntegerField()
  content_object  = GenericForeignKey('content_type', 'object_id')
  ip_address      = models.CharField(max_length=220, blank=True, null=True)
  timestamp       = models.DateTimeField(auto_now_add=True)

  def __str__(self, ):
    return "%s viewed on: %s" %(self.content_object, self.timestamp)

  class Meta:
    ordering = ['-timestamp']
    verbose_name = 'Object Viewed'
    verbose_name_plural = 'Objects Viewed'


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
  c_type = ContentType.objects.get_for_model(sender) # == instance.__class__
  new_view_obj = ObjectViewed.objects.create(
    user=request.user,
    object_id=instance.id,
    content_type=c_type,
    ip_address=get_client_ip(request),

  )

object_viewed_signal.connect(object_viewed_receiver)






class UserSession(models.Model):
  user            = models.ForeignKey(User, blank=True, null=True)
  ip_address      = models.CharField(max_length=220, blank=True, null=True)
  session_key     = models.CharField(max_length=100, blank=True, null=True)
  timestamp       = models.DateTimeField(auto_now_add=True)
  active          = models.BooleanField(default=True)
  ended           = models.BooleanField(default=False)

  def __str__(self, ):
    return str(self.session_key)



def user_logged_in_receiver(sender, instance, request, *args, **kwargs):
  print(instance)

user_logged_in.connect(user_logged_in_receiver)