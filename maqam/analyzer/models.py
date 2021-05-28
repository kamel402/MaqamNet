from django.db import models

# Create your models here.
class QuranFile(models.Model):

    quran_file = models.FileField()

    def __str__(self):
        return f'file {self.quran_file}'
