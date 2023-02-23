from django import forms
from .models import body, patient, phenotype

class VCFSequenceForm(forms.ModelForm):
    class Meta:
        model = body
        fields = ('chrom', 'pos', 'id1', 'ref', 'alt', 'qual', 'filter', 'info')


class VCFInsertForm(forms.Form):
    vcf_file = forms.FileField(label='Select VCF file')


class InsertPatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ('person_id', 'age', 'gender')

class InsertPhenotypeForm(forms.ModelForm):
    class Meta:
        model = phenotype
        fields = ('person_id', 'phenotype_description')