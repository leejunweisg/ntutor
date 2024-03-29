from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

# one user mapped to one profile
class Profile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, null=True)
    verified = models.IntegerField(default=0)
    description = models.TextField(null=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    # override parent class's save(), to resize image on save
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # resize uploaded image and overwrite
        img = Image.open(self.image)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.name)