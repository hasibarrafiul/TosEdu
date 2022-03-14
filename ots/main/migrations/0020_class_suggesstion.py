# Generated by Django 3.2.6 on 2022-03-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_english_docquestions_paper'),
    ]

    operations = [
        migrations.CreateModel(
            name='class_suggesstion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.IntegerField(choices=[(1, 'Class One'), (2, 'Class Two'), (3, 'Class Three'), (4, 'Class Four'), (5, 'Class Five'), (6, 'Class Six'), (7, 'Class Seven'), (8, 'Class Eight'), (9, 'Class Nine'), (10, 'Class Ten')], default=None, null=True)),
                ('date', models.DateField()),
                ('bangla', models.CharField(blank=True, max_length=100, null=True)),
                ('english', models.CharField(blank=True, max_length=100, null=True)),
                ('math', models.CharField(blank=True, max_length=100, null=True)),
                ('science', models.CharField(blank=True, max_length=100, null=True)),
                ('social', models.CharField(blank=True, max_length=100, null=True)),
                ('islamReligion', models.CharField(blank=True, max_length=100, null=True)),
                ('hinduReligion', models.CharField(blank=True, max_length=100, null=True)),
                ('boudhuReligion', models.CharField(blank=True, max_length=100, null=True)),
                ('cristantianReligion', models.CharField(blank=True, max_length=100, null=True)),
                ('artsAndCrafts', models.CharField(blank=True, max_length=100, null=True)),
                ('physicalEducation', models.CharField(blank=True, max_length=100, null=True)),
                ('music', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]