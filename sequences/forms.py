from django import forms
from .models import Body

class VCFSequenceForm(forms.ModelForm):
    class Meta:
        model = Body
        fields = ('chrom', 'pos', 'id1', 'ref', 'alt', 'qual', 'filter', 'info')



class VCFInsertForm(forms.Form):
    vcf_file = forms.FileField(label='Select VCF file')