from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class RecipePhoto(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # image = models.ImageField(upload_to='recipes/')
    image = CloudinaryField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')

    class Meta:
        ordering = ['-uploaded_at']
        permissions = [
            ('can_edit_all_photos', 'Can edit all photos'),
            ('can_delete_all_photos', 'Can delete all photos'),
        ]

    def __str__(self):
        return self.title