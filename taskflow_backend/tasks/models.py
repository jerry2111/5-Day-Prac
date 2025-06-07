from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, 
                              related_name='tasks' , 
                              null=True,  # ✅ ให้ค่า null ได้
                              blank=True  # ✅ ให้กรอกในฟอร์มว่างได้ (สำหรับ admin หรือ DRF)
                             )

    def __str__(self):
        return self.title
