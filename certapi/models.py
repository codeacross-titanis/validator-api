from django.db import models

from model_utils.models import TimeStampedModel


class Student(TimeStampedModel):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Educator(TimeStampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    logo = models.ImageField()
    url = models.URLField()


    def __str__(self):
        return self.name


class Certification(TimeStampedModel):
    name = models.CharField(max_length=255)
    eduator = models.ForeignKey(Educator)

    def __str__(self):
        return self.name


class CompletedCertification(TimeStampedModel):
    student = models.ForeignKey(Student)
    certification = models.ForeignKey(Certification)
