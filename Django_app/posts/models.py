from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

# Create your models here.

class UserPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    text = models.CharField(max_length=1024, blank=True)
    file = models.FileField(upload_to='upload', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def clean(self):
        if not (self.text or self.file):
            raise ValidationError("You must specify either text or file")
    def get_file_url(self):
        if self.file:
            return self.file.url
        return None
    
class UserFollowers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')  
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')  
    created_at = models.DateTimeField(auto_now_add=True)

class UserSubscriptions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')  
    subscribed_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribed_to')  
    created_at = models.DateTimeField(auto_now_add=True)