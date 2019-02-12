from django.db import models

# Create your models here.

class photo (models.Model):
    img=models.ImageField(upload_to='img/')
    sharing=models.BooleanField(default=False)
    def share(self):
        self.sharing=True