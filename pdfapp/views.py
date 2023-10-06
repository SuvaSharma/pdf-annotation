from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.contrib.auth.models import User 
from .models import PDFFile, User, Post
from django.contrib import messages
from .forms import PDFFileForm
import uuid
from django.urls import reverse
import fitz  # PyMuPDF
import io
import json

def home(request):
    return render(request, 'home.html')

# Login System
class LoginView(ListView):
    def get(self, request):
        return redirect('home')

    def post(self, request):
        user_name = request.POST['uname']
        pwd = request.POST['pwd']

   

        user_exists = User.objects.filter(username=user_name, password=pwd).exists()
        if user_exists:
            request.session['user'] = user_name
            messages.success(request, 'You are logged in successfully.')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Username or Password.')
            return redirect('home')
     

class LogoutView(ListView):
    def get(self, request):
        try:
            del request.session['user']
        except:
            return redirect('home') 
        return redirect('home')




def upload_pdf(request):
    if request.method == 'POST':
        form = PDFFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            pdfs = PDFFile.objects.all()
            return render(request, 'pdf_list.html', {'pdfs': pdfs})
    else:
        form = PDFFileForm()
    return render(request, 'upload.html', {'form': form})

def view_pdf(request, pk):
    pdf_file = get_object_or_404(PDFFile, pk=pk)
    pdf_path = pdf_file.pdf.path
    print(pdf_path)
    return HttpResponse(open(pdf_path, 'rb').read(), content_type='application/pdf')

def list_pdfs(request):
    pdfs = PDFFile.objects.all()
    return render(request, 'pdf_list.html', {'pdfs': pdfs})

def edit_pdf(request, pk):
    pdf_file = get_object_or_404(PDFFile, pk=pk)
    pdf_path = pdf_file.pdf.path
    print(pdf_file.pdf.url)
    if request.method == 'POST':
        print("POST REQUEST")
        annotations = request.POST.get('annotations', '')

        

        # PDF using PyMuPDF
        pdf_document = fitz.open(pdf_path)

       
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            page.add_textbox((100, 100, 400, 400), annotations)

        
        edited_pdf_path = pdf_path.replace(".pdf", "_edited.pdf")
        pdf_document.save(edited_pdf_path)
        pdf_document.close()

        # Update gareko annotation lai
        pdf_file.annotations = annotations
        pdf_file.save()

        response_data = {'success': True, 'edited_pdf_path': edited_pdf_path}
        return JsonResponse(response_data)

    return render(request, 'pdf_annotation.html', {'pdf_file_url': pdf_file.pdf.url,'pdf_instance': pdf_file})


from django.http import JsonResponse

from django.http import JsonResponse
from .models import PDFFile  

def save_pdf(request, pdf_id):
    if request.method == 'POST':
        pdf_instance = PDFFile.objects.get(pk=pdf_id)
        pdf_file = request.FILES.get('pdf_file')

        if pdf_file:
            pdf_instance.pdf = pdf_file
            pdf_instance.save()

            # Check if the annotated PDF URL is already generated
            if not pdf_instance.annotated_pdf_url:
                unique_url = str(uuid.uuid4())
                pdf_instance.annotated_pdf_url = reverse('view_annotated_pdf', args=[unique_url])
                pdf_instance.save()

            return JsonResponse({'success': True, 'annotated_pdf_url': pdf_instance.annotated_pdf_url})
        else:
            return JsonResponse({'success': False, 'error': 'No PDF file received.'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  
def save_annotations(request, pk):
    if request.method == 'POST':
        try:
        
            annotated_pdf_data = request.POST.get('annotated_pdf_data')
            
            annotated_pdf, created = PDFFile.objects.update_or_create(
                pk=pk,
                defaults={'pdf_data': annotated_pdf_data}
            )

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


from django.shortcuts import render, get_object_or_404
from .models import PDFAnnotation

def generate_pdf_annotation(request):
    # Generate a unique token
    import random
    import string
    unique_token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # Create a new PDFAnnotation instance with the token
    pdf_annotation = PDFAnnotation.objects.create(token=unique_token, pdf_data="")

    # Return the URL with the unique token
    return render(request, 'pdf_annotation.html', {'token': unique_token})

def view_pdf_annotation(request, token):
    # Retrieve the PDF annotation data based on the token
    pdf_annotation = get_object_or_404(PDFAnnotation, token=token)

    # Serve the PDF annotation page with data
    return render(request, 'pdf_annotation.html', {'pdf_data': pdf_annotation.pdf_data})