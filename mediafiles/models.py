from django.db import models


from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Photo(models.Model):
    image = models.ImageField(upload_to="photos")
    caption = models.CharField(max_length=255, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.caption or str(self.image)
