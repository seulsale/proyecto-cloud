from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TODO(models.Model):
    owner = models.ForeignKey(User, models.CASCADE)
    text = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.text

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
