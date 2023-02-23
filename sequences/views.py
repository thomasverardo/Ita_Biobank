import vcfpy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import body, file_description, sample_info, patient, phenotype
from .forms import VCFInsertForm, InsertPatientForm, InsertPhenotypeForm
from datetime import datetime
import csv
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages


class AuthenticationLogin(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

@login_required
def display_sequences(request):
    # insert_data(request)
    sequences = body.objects.all()
    file_description_ = file_description.objects.all()
    sample_info_ = sample_info.objects.all()
    patients = patient.objects.all()
    pheno = phenotype.objects.all()
    return render(request, 'sequences/display_sequences.html', {'sequences': sequences, 
                                                                'file_description': file_description_, 
                                                                'sample_info': sample_info_,
                                                                'patients': patients,
                                                                'phenotype': pheno
                                                                })
    # return render(request, 'sequences/table_sequences.html', {'table': Sample_table})


def export_csv(request):
    # query = body.objects.select_related('file_description').all()
    query = body.objects.all()
    filename = "export_csv_biobank"
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

    writer = csv.writer(response)
    writer.writerow([field.name for field in query.model._meta.fields])

    for obj in query:
        writer.writerow([getattr(obj, field.name) for field in query.model._meta.fields])

    return response


def add_patient(request):
    if request.method == 'POST':
        form = InsertPatientForm(request.POST)
        if form.is_valid():
            person_id = form.cleaned_data['person_id']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']

            # Insert data into the person table
            person = patient(person_id=person_id, age=age, gender=gender)
            person.save()
            return redirect('/sequences/')
    else:
        form = InsertPatientForm()
    return render(request, 'sequences/add_patient.html', {'form': form})

def add_phenotype(request):
    if request.method == 'POST':
        form = InsertPhenotypeForm(request.POST)
        if form.is_valid():
            person_id = form.cleaned_data['person_id']
            phenotype_description = form.cleaned_data['phenotype_description']

            # Insert data into the phenotype table
            phenotype_new = phenotype(person_id=person_id, phenotype_description=phenotype_description)
            phenotype_new.save()
            return redirect('/sequences/')
    else:
        form = InsertPhenotypeForm()
    return render(request, 'sequences/add_phenotype.html', {'form': form})



def insert_vcf_file(request):
    form = VCFInsertForm()
    if request.method == 'POST':
        form = VCFInsertForm(request.POST, request.FILES)
        if form.is_valid():
            vcf_file = form.cleaned_data['vcf_file']
            # Perform logic to insert VCF file into database
            insert_data_from_file(request, vcf_file)
            # ...
            return redirect('display_sequences')
    return render(request, 'sequences/display_sequences.html', {'form': form})


def insert_data_from_file(request, vfc_file):

    reader = vcfpy.Reader.from_path(vfc_file)

    username = str(request.user)
    file_id_new = username + "_" + datetime.now().strftime('%F %T.%f')

    header_lines = reader.header.lines

    new_file_description = file_description(
        file_id = file_id_new,
        file_format = header_lines[0].value,
        file_data = header_lines[1].value,
        source = header_lines[2].value,
        reference = header_lines[3].value,
        contig = header_lines[4].value,
        phasing = header_lines[5].value
    )
    new_file_description.save() #Save into database postgresql

    # for line in header_lines:
    #     print(line.value)

    for record in reader:
        new_sequence = body(
            file_id1 = file_id_new,
            file_description = new_file_description,
            chrom = record.CHROM, 
            pos = record.POS, 
            id1 = record.ID, 
            ref = record.REF, 
            alt = record.ALT, 
            qual = record.QUAL, 
            filter = record.FILTER, 
            info = record.INFO
            )

        try:
            new_sequence.save()
        except Exception as e:
            print(f"Error saving: {e}")


        for person in record.calls:
            # excluded = {k: person[k] for k in set(list(person.sample)) - set(['GT', 'GQ'])}
            
            for key, value in person.data.items():
                if key == 'GT':
                    gt = value
                if key == 'GQ':
                    gq = value
                else:
                    other = value

            new_sample_info = sample_info(
                file_id1 = file_id_new,
                # person_id = person.sample,
                body_id = new_sequence,
                format_gt = gt,
                format_gq = gq,
                all_other = other
                # file_description = new_file_description
            )

            new_sample_info.save()


        # print(new_sequence.chrom)
    reader.close()

def insert_data(request):

    try:

        reader = vcfpy.Reader.from_path('spec.vcf')

        username = str(request.user)
        file_id_new = username + "_" + datetime.now().strftime('%F %T.%f')

        header_lines = reader.header.lines

        new_file_description = file_description(
            file_id = file_id_new,
            file_format = header_lines[0].value,
            file_data = header_lines[1].value,
            source = header_lines[2].value,
            reference = header_lines[3].value,
            contig = header_lines[4].value,
            phasing = header_lines[5].value
        )
        new_file_description.save() #Save into database postgresql

        # for line in header_lines:
        #     print(line.value)

        for record in reader:
            new_sequence = body(
                file_id1 = file_id_new,
                File_description = new_file_description,
                chrom = record.CHROM, 
                pos = record.POS, 
                id1 = record.ID, 
                ref = record.REF, 
                alt = record.ALT, 
                qual = record.QUAL, 
                filter = record.FILTER, 
                info = record.INFO
                )

            try:
                new_sequence.save()
            except Exception as e:
                print(f"Error saving: {e}")


            for person in record.calls:
                # excluded = {k: person[k] for k in set(list(person.sample)) - set(['GT', 'GQ'])}
                
                for key, value in person.data.items():
                    if key == 'GT':
                        gt = value
                    if key == 'GQ':
                        gq = value
                    else:
                        other = value

                new_sample_info = sample_info(
                    file_id1 = file_id_new,
                    # person_id = person.sample,
                    format_gt = gt,
                    format_gq = gq,
                    all_other = other,
                    File_description = new_file_description
                )

                new_sample_info.save()


            # print(new_sequence.chrom)
        reader.close()

        # print("file closed")

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error as ", e)
