# Generated by Django 5.1.4 on 2024-12-24 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_resume"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BlogPostComment",
        ),
    ]