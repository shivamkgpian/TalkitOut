# Generated by Django 3.2.9 on 2022-12-06 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20221206_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcements',
            old_name='announce',
            new_name='description',
        ),
    ]