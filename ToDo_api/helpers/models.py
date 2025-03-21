from django.db import models

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # This will not create a table for this model
        ordering = ('-created_at',) # This will order the data in descending order of created_at    