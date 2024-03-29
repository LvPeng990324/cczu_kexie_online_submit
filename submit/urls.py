from django.urls import path
from . import views


urlpatterns = [
    path('submit/<name>/<class_num>/<phone>/<qq_num>/<department>/', views.submit),
    path('new_person_request/', views.new_person_request),
    path('new_person_submit/', views.new_person_submit, name='new_person'),
    path('kexie_person_request/', views.kexie_person_request),
    path('kexie_person_submit/', views.kexie_person_submit, name='kexie_person'),
]

