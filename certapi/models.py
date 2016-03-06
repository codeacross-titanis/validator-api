from django.db import models

from model_utils.models import TimeStampedModel


class Student(TimeStampedModel):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Provider(TimeStampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    logo = models.ImageField()
    url = models.URLField()


    def __str__(self):
        return self.name


class Badge(TimeStampedModel):
    name = models.CharField(max_length=255)
    student = models.ForeignKey(Student)
    description = models.TextField()
    completed_date = models.DateField()
    is_validated = models.BooleanField(default=False)
    validated_at = models.DateField(null=True, blank=True)
    validated_by = models.ForeignKey(Provider, null=True, blank=True)
    logo = models.URLField()

    def __str__(self):
        return self.name
