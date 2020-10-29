from django.db import models


# Create your models here.

class ShortenedUrl(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(unique=True, db_index=True)
    clicks_count = models.IntegerField(default=0)
