# Generated by Django 3.2.6 on 2022-01-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='chapter',
            field=models.IntegerField(choices=[(1, 'Chapter One'), (2, 'Chapter Two'), (3, 'Chapter Three'), (4, 'Chapter Four'), (5, 'Chapter Five'), (6, 'Chapter Six'), (7, 'Chapter Seven'), (8, 'Chapter Eight'), (9, 'Chapter Nine'), (10, 'Chapter Ten')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='classes',
            field=models.IntegerField(choices=[(1, 'Class One'), (2, 'Class Two'), (3, 'Class Three'), (4, 'Class Four'), (5, 'Class Five'), (6, 'Class Six'), (7, 'Class Seven'), (8, 'Class Eight'), (9, 'Class Nine'), (10, 'Class Ten')], default=None, max_length=100, null=True),
        ),
    ]