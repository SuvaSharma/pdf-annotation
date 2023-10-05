from django import forms
from .models import PDFFile, PDFDocument

class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['title', 'pdf']

        class PDFDocumentForm(forms.ModelForm):
            class Meta:
                model = PDFDocument
                fields = ('title', 'pdf_file')
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")