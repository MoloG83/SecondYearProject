# Generated by Django 3.1.6 on 2021-04-24 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_slider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='slider',
            new_name='slide',
        ),
    ]