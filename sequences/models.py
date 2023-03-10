from django.db import models


class file_description(models.Model):
    file_id = models.CharField(max_length=100, primary_key=True)
    file_format = models.CharField(max_length=50)
    file_data = models.CharField(max_length=200)
    source = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)
    contig = models.CharField(max_length=255)
    phasing = models.CharField(max_length=40)



class body(models.Model):
    file_id1 = models.CharField(max_length=50)
    chrom = models.CharField(max_length=4)
    pos = models.IntegerField()
    id1 = models.CharField(max_length=30)
    ref = models.CharField(max_length=200)
    alt = models.CharField(max_length=200)
    qual = models.CharField(max_length=100, null=False)
    filter = models.CharField(max_length=100)
    info = models.CharField(max_length=255)

    file_description = models.ForeignKey(file_description, on_delete=models.RESTRICT)

    class Meta:
        app_label = 'sequences'


class sample_info(models.Model):
    file_id1 = models.CharField(max_length=50)
    person_id = models.CharField(max_length=50, default=None)
    format_gt = models.CharField(max_length=5)
    format_gq = models.CharField(max_length=5)
    all_other = models.CharField(max_length=100)

    body_id = models.ForeignKey(body, on_delete=models.RESTRICT, default=None)


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)

class patient(models.Model):
    person_id = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class phenotype(models.Model):
    phenotype_description = models.CharField(max_length=255, default=None)
    person_id = models.ForeignKey(patient, on_delete=models.RESTRICT)


class info(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    number = models.CharField(max_length=3)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=255)

class filter(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=255)

class format(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    number = models.CharField(max_length=3)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
