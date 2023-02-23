from django.urls import path
from sequences.views import display_sequences, insert_vcf_file, add_patient, export_csv, add_phenotype, AuthenticationLogin
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sequences/', display_sequences, name='display_sequences'),
    path('insert_vcf/', insert_vcf_file, name='insert_vcf_file'),
    path('add_person/', add_patient, name='add_person'),
    path('add_phenotype/', add_phenotype, name='add_phenotype'),
    path('export-csv/', export_csv, name='export_csv'),
    path('login/', AuthenticationLogin.as_view(), name='login'),
]