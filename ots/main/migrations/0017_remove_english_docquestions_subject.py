# Generated by Django 3.2.6 on 2022-03-01 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_english_docquestions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='english_docquestions',
            name='subject',
        ),
    ]
