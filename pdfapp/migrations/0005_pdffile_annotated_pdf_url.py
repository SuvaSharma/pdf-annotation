# Generated by Django 4.2.2 on 2023-10-02 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfapp', '0004_user_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdffile',
            name='annotated_pdf_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
