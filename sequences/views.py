import vcfpy
from django.shortcuts import render, redirect
from .models import Body, File_description, Sample_info
from .forms import VCFSequenceForm, VCFInsertForm
from datetime import datetime

def display_sequences(request):
    # insert_data(request)
    sequences = Body.objects.all()
    file_description = File_description.objects.all()
    sample_info = Sample_info.objects.all()
    return render(request, 'sequences/display_sequences.html', {'sequences': sequences, 'file_description': file_description, 'sample_info': sample_info})

def submit_sequence(request):
    if request.method == 'POST':
        form = VCFSequenceForm(request.POST)
        if form.is_valid():
            form.save()
            print("SUBMIT")
            return redirect('display_sequences')
    else:
        form = VCFSequenceForm()
    return render(request, 'sequences/submit_sequence.html', {'form': form})


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

    new_file_description = File_description(
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
        new_sequence = Body(
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

            new_sample_info = Sample_info(
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

def insert_data(request):

    try:

        reader = vcfpy.Reader.from_path('spec.vcf')

        username = str(request.user)
        file_id_new = username + "_" + datetime.now().strftime('%F %T.%f')

        header_lines = reader.header.lines

        new_file_description = File_description(
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
            new_sequence = Body(
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

                new_sample_info = Sample_info(
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
