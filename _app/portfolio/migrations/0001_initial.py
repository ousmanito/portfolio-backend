# Generated by Django 5.1.4 on 2024-12-08 01:25

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("title_en", models.CharField(max_length=200, null=True)),
                ("title_fr", models.CharField(max_length=200, null=True)),
                ("url", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="LifeEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, null=True)),
                ("title_en", models.CharField(max_length=200, null=True)),
                ("title_fr", models.CharField(max_length=200, null=True)),
                ("entity", models.CharField(max_length=200, null=True)),
                ("entity_en", models.CharField(max_length=200, null=True)),
                ("entity_fr", models.CharField(max_length=200, null=True)),
                ("description", models.TextField(null=True)),
                ("description_en", models.TextField(null=True)),
                ("description_fr", models.TextField(null=True)),
                ("date", models.DateField(null=True)),
                ("kind", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Mail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=400, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, null=True)),
                ("title_en", models.CharField(max_length=200, null=True)),
                ("title_fr", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("title_en", models.CharField(max_length=200, null=True)),
                ("title_fr", models.CharField(max_length=200, null=True)),
                ("resume", models.TextField()),
                ("resume_en", models.TextField(null=True)),
                ("resume_fr", models.TextField(null=True)),
                ("body", models.TextField()),
                ("body_en", models.TextField(null=True)),
                ("body_fr", models.TextField(null=True)),
                ("creation_date", models.DateField(default=datetime.datetime.now)),
                ("image", models.ImageField(null=True, upload_to="blog/")),
                ("url", models.CharField(max_length=200)),
                ("categories", models.ManyToManyField(to="portfolio.blogcategory")),
            ],
        ),
        migrations.CreateModel(
            name="BlogPostComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("creation_date", models.DateTimeField(default=datetime.datetime.now)),
                ("count", models.PositiveIntegerField(default=0)),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="portfolio.blogpost",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replies",
                        to="portfolio.blogpostcomment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, null=True)),
                ("title_en", models.CharField(max_length=200, null=True)),
                ("title_fr", models.CharField(max_length=200, null=True)),
                ("description", models.TextField(null=True)),
                ("description_en", models.TextField(null=True)),
                ("description_fr", models.TextField(null=True)),
                (
                    "order",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=1)
                        ]
                    ),
                ),
                ("image", models.ImageField(null=True, upload_to="services/")),
                ("details", models.ManyToManyField(to="portfolio.skill")),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, null=True)),
                ("title_en", models.CharField(max_length=200, null=True)),
                ("title_fr", models.CharField(max_length=200, null=True)),
                ("short_description", models.CharField(max_length=200, null=True)),
                ("short_description_en", models.CharField(max_length=200, null=True)),
                ("short_description_fr", models.CharField(max_length=200, null=True)),
                ("description", models.TextField(null=True)),
                ("description_en", models.TextField(null=True)),
                ("description_fr", models.TextField(null=True)),
                (
                    "order",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=1)
                        ]
                    ),
                ),
                ("url", models.CharField(blank=True, max_length=300, null=True)),
                ("github", models.CharField(blank=True, max_length=300, null=True)),
                ("skills", models.ManyToManyField(to="portfolio.skill")),
            ],
        ),
    ]
