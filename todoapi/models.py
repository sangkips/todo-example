from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=150)
    completed = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return self.title

