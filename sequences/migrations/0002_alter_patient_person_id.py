# Generated by Django 4.1.5 on 2023-02-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='person_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
