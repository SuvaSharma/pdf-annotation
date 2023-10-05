from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'), 
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('pdf/<int:pk>/', views.view_pdf, name='view_pdf'),
    path('pdfs/', views.list_pdfs, name='list_pdfs'),

    path('edit_pdf/<int:pk>/', views.edit_pdf, name='edit_pdf'),
    path('save_pdf/<int:pdf_id>/', views.save_pdf, name='save_pdf'),
    path('save_annotations/<int:pk>/', views.save_annotations, name='save_annotations'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)