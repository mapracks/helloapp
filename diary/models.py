from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Entry(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    text = models.TextField()
    title = models.TextField()
    mood = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('description' ,kwargs={'pk' : self.pk})
    
    class Meta:
        verbose_name_plural = 'Entries'

    