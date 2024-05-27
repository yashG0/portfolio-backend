from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    project_img = models.ImageField(upload_to='project_images/')
    project_source_code = models.URLField()

    def __str__(self):
        return self.project_name


class FormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=32, default='testing@example.com')
    message = models.TextField(max_length=2000, default="this is testing message")
    
    def __str__(self):
        return self.name