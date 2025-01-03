from datetime import datetime

from django.conf import settings
from django.db import models
from django.db.models.expressions import F
from django_minio_backend import MinioBackend
from rest_framework.fields import MinValueValidator

file_storage = None

if settings.ENVIRONMENT == "production":
    file_storage = MinioBackend(bucket_name=settings.MINIO_MEDIA_FILES_BUCKET)


class Resume(models.Model):
    file = models.FileField(
        upload_to="resume/",
        storage=file_storage,
    )


class BlogCategory(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return str(self.title)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(BlogCategory)
    resume = models.TextField()
    body = models.TextField()
    creation_date = models.DateField(default=datetime.now)
    image = models.ImageField(
        upload_to="blog/",
        storage=file_storage,
        null=True,
    )
    url = models.CharField(max_length=200)

    def __str__(self):
        return str(self.title)


class LifeEvent(models.Model):
    title = models.CharField(max_length=200, null=True)
    entity = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True)
    kind = models.CharField(max_length=200)

    def __str__(self):
        return str(self.title)


class Skill(models.Model):
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.title)


class Service(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    details = models.ManyToManyField(Skill)
    order = models.PositiveIntegerField(validators=[MinValueValidator(limit_value=1)])
    image = models.ImageField(
        upload_to="services/",
        storage=file_storage,
        null=True,
    )

    def __str__(self):
        return str(self.title)


class Project(models.Model):
    title = models.CharField(max_length=200, null=True)
    short_description = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    order = models.PositiveIntegerField(validators=[MinValueValidator(limit_value=1)])
    url = models.CharField(max_length=300, null=True, blank=True)
    github = models.CharField(max_length=300, null=True, blank=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return str(self.title)


class Mail(models.Model):
    email = models.CharField(max_length=400, unique=True)
