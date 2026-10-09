from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    role=models.CharField(max_length=20,choices=[('STUDENT','student'),('ADMIN','admin'),('SUPERADMIN','superadmin')],default='STUDENT',)
    is_approved=models.BooleanField(default=False)
    face_image=models.ImageField(upload_to='student_faces/',blank=False,null=False)
    
    def __str__(self):
        return self.username
