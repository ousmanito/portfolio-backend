# Generated by Django 4.2.3 on 2023-10-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='short_description',
            field=models.CharField(default='---', max_length=200),
            preserve_default=False,
        ),
    ]
