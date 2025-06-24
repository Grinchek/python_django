from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from django.utils import timezone
from tinymce.models import HTMLField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            webp_path = os.path.splitext(self.image.path)[0] + '.webp'
            img = img.convert('RGB')
            img.save(webp_path, 'webp', quality=70, optimize=True)
            if self.image.path != webp_path:
                os.remove(self.image.path)
            self.image.name = os.path.splitext(self.image.name)[0] + '.webp'
            self.image.file = open(webp_path, 'rb')
            super().save(update_fields=['image'])

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
