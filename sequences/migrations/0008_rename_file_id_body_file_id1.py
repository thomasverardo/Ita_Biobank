# Generated by Django 4.1.5 on 2023-02-07 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sequences', '0007_alter_body_file_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='body',
            old_name='file_id',
            new_name='file_id1',
        ),
    ]