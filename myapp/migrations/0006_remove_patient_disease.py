# Generated by Django 4.2.1 on 2023-06-12 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='disease',
        ),
    ]
