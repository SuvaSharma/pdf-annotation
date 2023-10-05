from django.db import models
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file_field = models.FileField(upload_to='uploads/')
    desc = models.TextField()

    def __str__(self):
        return f'{self.user}=> {self.title}'

class PDFFile(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')
    upload_date = models.DateTimeField(auto_now_add=True)
    annotations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    
class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title
    
class UploadedPDF(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')

    # models.py
from django.db import models

class PDFAnnotation(models.Model):
    token = models.CharField(max_length=10, unique=True)
    pdf_data = models.TextField()
