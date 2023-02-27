
# Ita biobank

In this repository it's shown the implementation of a national biobank for storing gene sequence variations in a standardized way (it stores only data from VCF format).

Biobanks are defined as collections of biological samples and associated information organised in a systematic way.

Storing gene sequence variations allows us to significantly reduce the size of data, while keeping a large amount of information since variations are considered the most important regions of DNA to study the genomic diseases and predispositions to diseases.

The project is entire built using Django, since it allows to create a database with PostgreSQL and the web application simultaneously.

## Required packages
```cmd
Django==3.1.2
vcfpy==0.13.6
```

## Usage

Run the following code

```cmd
python3 manage.py runserver 127.0.0.1:8000
```

## Cloud

The web application built with this code will run in an Amazon EC2 instance.

