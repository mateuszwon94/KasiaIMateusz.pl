from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/") # upload image file to ./media/images/ directory

    def summary(self):
        return self.body[:100]
    
    def __str__(self):
        return self.title