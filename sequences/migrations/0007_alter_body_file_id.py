# Generated by Django 4.1.5 on 2023-02-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequences', '0006_file_description_body_file_id_body_file_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body',
            name='file_id',
            field=models.CharField(max_length=50),
        ),
    ]