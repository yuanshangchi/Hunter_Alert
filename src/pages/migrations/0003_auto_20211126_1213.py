# Generated by Django 3.1.4 on 2021-11-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20211126_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dept_name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='requirement',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='yourname',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
