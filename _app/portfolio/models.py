from django.db import models
from datetime import datetime

from django.db.models.expressions import F


class Mail(models.Model):
    email = models.CharField(max_length=400, unique=True)


class BlogCategory(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(BlogCategory)
    resume = models.CharField(max_length=200)
    body = models.TextField()
    creation_date = models.DateField(default=datetime.now)
    image = models.FileField(upload_to="blog/")
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now)
    count = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies", null=True
    )

    def increment_count(self):
        self.count = F("count") + 1
        self.save()
        self.refresh_from_db()

    def decrement_count(self):
        self.count = F("count") - 1
        self.save()
        self.refresh_from_db()

    def __str__(self):
        return f"Commentaire de {self.first_name} {self.last_name} sur {self.blog}"


class Skill(models.Model):
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


class Expertise(models.Model):
    title = models.CharField(max_length=200, null=True)
    skill = models.ManyToManyField(Skill, related_name="expertises")
    order = models.IntegerField(default=0)
    image = models.FileField(upload_to="expertises/", null=True)
    url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class ServiceDetail(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    short_description = models.CharField(max_length=200, null=True)
    details = models.ManyToManyField(ServiceDetail)
    order = models.IntegerField(default=0)
    image = models.FileField(upload_to="services/", null=True)
    url = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.title


class Projet(models.Model):
    title = models.CharField(max_length=200, null=True)
    short_description = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    order = models.IntegerField(default=0)
    url = models.CharField(max_length=300, null=True, blank=True)
    github = models.CharField(max_length=300, null=True, blank=True)
    skill = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200, null=True)
    client = models.CharField(max_length=200, null=True)
    contract_type = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    location = models.CharField(max_length=200, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=200, null=True)
    school_name = models.CharField(max_length=200, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class SoftSkill(models.Model):
    skill = models.ForeignKey(
        Skill, related_name="skills", on_delete=models.CASCADE, null=True
    )
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.skill.title


class Language(models.Model):
    skill = models.ForeignKey(
        Skill, related_name="languages", on_delete=models.CASCADE, null=True
    )
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.skill.title
