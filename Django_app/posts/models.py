from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

# Create your models here.

class UserPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    text = models.CharField(max_length=1024, blank=True)
    image = models.ImageField(upload_to='upload/imgs', blank=True)
    video = models.FileField(upload_to='upload/videos', blank=True)
    file = models.FileField(upload_to='upload/files', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,blank =True, related_name='liked_by')
    def clean(self):
        if not (self.text or self.image or self.video or self.file):
            raise ValidationError("You must specify at least one field")
    

class UserFollowers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')  
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')  
    created_at = models.DateTimeField(auto_now_add=True)

class UserSubscriptions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')  
    subscribed_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribed_to')  
    created_at = models.DateTimeField(auto_now_add=True)