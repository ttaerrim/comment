# Generated by Django 3.1 on 2020-08-31 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
