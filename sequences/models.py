from django.db import models
import django_tables2 as tables


class File_description(models.Model):
    file_id = models.CharField(max_length=100, primary_key=True)
    file_format = models.CharField(max_length=50)
    file_data = models.CharField(max_length=20)
    source = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    contig = models.CharField(max_length=255)
    phasing = models.CharField(max_length=40)



class Body(models.Model):
    file_id1 = models.CharField(max_length=50)
    
    chrom = models.CharField(max_length=4)
    pos = models.IntegerField()
    id1 = models.CharField(max_length=30)
    ref = models.CharField(max_length=200) #Only 20 or more??? Or less?
    alt = models.CharField(max_length=200)
    # qual = models.IntegerField(max_length=10)
    qual = models.CharField(max_length=100)
    filter = models.CharField(max_length=100)
    info = models.CharField(max_length=255)

    File_description = models.ForeignKey(File_description, on_delete=models.RESTRICT)

    class Meta:
        app_label = 'sequences'
        attrs = {"class": "mytable"}


class Sample_info(models.Model):
    file_id1 = models.CharField(max_length=50)
    # person_id = models.CharField(max_length=50)

    format_gt = models.CharField(max_length=5)
    format_gq = models.CharField(max_length=5)
    all_other = models.CharField(max_length=100)

    File_description = models.ForeignKey(File_description, on_delete=models.RESTRICT)


table = Body()
