# Generated by Django 4.1.5 on 2023-02-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequences', '0004_delete_file_description_remove_body_file_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body',
            name='alt',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='body',
            name='ref',
            field=models.CharField(max_length=200),
        ),
    ]
