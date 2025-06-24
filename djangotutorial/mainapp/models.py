from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # Зберегти початкове зображення
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # Створити шлях до .webp
            webp_path = os.path.splitext(self.image.path)[0] + '.webp'

            # Конвертація в RGB та збереження у форматі webp
            img = img.convert('RGB')
            img.save(webp_path, 'webp', quality=70, optimize=True)

            # Видалити оригінальний файл (jpg/png)
            if self.image.path != webp_path:
                os.remove(self.image.path)

            # Оновити шлях у полі image
            self.image.name = os.path.splitext(self.image.name)[0] + '.webp'
            self.image.file = open(webp_path, 'rb')

            # Повторно зберегти модель з новим зображенням
            super().save(update_fields=['image'])
