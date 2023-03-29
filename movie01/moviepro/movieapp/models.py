from django.db import models

# Create your models here.
class table(models.Model):
    image = models.ImageField(upload_to='img', null=True)
    name = models.CharField(max_length=150)
    date = models.DateField()
    about = models.TextField()

    def __str__(self):
        return self.name