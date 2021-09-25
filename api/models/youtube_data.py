from django.db import models
from django.db.models import JSONField


class YoutubeData(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    published_at = models.DateTimeField(db_index=True)
    thumbnails = JSONField(default=dict, blank=True, null=True)

    video_id = models.CharField(max_length=255, db_index=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']
        app_label = 'api'

    def __str__(self):
        return self.title

    @property
    def video_url(self):
        return " ".join(["https://www.youtube.com/watch?v=", self.video_id])
