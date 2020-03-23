from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TODO(models.Model):
    owner = models.ForeignKey(User, models.CASCADE)
    text = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(blank=True)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(TODO, self).save(*args, **kwargs)
