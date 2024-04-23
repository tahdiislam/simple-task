from django.db import models
from categories.models import Category


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=200, blank=False)
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField(blank=False)
    category = models.ManyToManyField(Category, default=None, blank=False)

    def __str__(self) -> str:
        return f"{self.title}"
