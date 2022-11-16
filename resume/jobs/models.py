import uuid
from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    total_votes = models.IntegerField(default=0, null=True, blank=True)
    votes_ratio = models.IntegerField(default=0, null=True, blank=True)
    demo_link = models.CharField(max_length=500, null=True, blank=True)
    source_link = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
