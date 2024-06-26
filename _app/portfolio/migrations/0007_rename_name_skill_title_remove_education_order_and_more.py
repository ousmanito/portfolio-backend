# Generated by Django 4.2.3 on 2023-10-19 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_education_order_experience_order_expertise_order_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='education',
            name='order',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='order',
        ),
        migrations.RemoveField(
            model_name='expertise',
            name='order',
        ),
        migrations.RemoveField(
            model_name='language',
            name='order',
        ),
        migrations.RemoveField(
            model_name='service',
            name='order',
        ),
        migrations.RemoveField(
            model_name='servicedetail',
            name='order',
        ),
        migrations.RemoveField(
            model_name='softskill',
            name='order',
        ),
    ]
