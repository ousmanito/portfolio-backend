# Generated by Django 4.2.6 on 2023-10-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_experience_description_experience_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='client',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='short_description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
