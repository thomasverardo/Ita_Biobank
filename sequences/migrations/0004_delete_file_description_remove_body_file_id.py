# Generated by Django 4.1.5 on 2023-02-07 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sequences', '0003_rename_sequence_body_body'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File_description',
        ),
        migrations.RemoveField(
            model_name='body',
            name='file_id',
        ),
    ]