from django.db import models

# Create your models here.
class Job(models.Model):
  title = models.CharField(max_length=20, blank=True, null=True)
  location = models.CharField(max_length=20, blank=True, null=True)
  title_id = models.CharField(max_length=50, blank=True, null=True)
  normalized_title = models.CharField(max_length=50, blank=True, null=True)

  def __str__(self):
    return self.normalized_title
