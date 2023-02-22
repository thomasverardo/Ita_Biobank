"""biobank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from sequences.views import display_sequences, insert_vcf_file, add_patient, export_csv

urlpatterns = [
    path('sequences/', display_sequences, name='display_sequences'),
    path('insert_vcf/', insert_vcf_file, name='insert_vcf_file'),
    path('add/', add_patient, name='add_person'),
    path('export-csv/', export_csv, name='export_csv')
]