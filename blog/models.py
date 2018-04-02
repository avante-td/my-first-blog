from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=200)
    text = models.TextField('Texto')
    created_date = models.DateTimeField('Data de criação', default=timezone.now)
    published_date = models.DateTimeField('Data de publicação', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
