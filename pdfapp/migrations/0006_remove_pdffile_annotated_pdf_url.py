# Generated by Django 4.2.2 on 2023-10-04 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdfapp', '0005_pdffile_annotated_pdf_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdffile',
            name='annotated_pdf_url',
        ),
    ]
