from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("students/", views.student_list, name='students'),
    path("coaches/", views.coaches_list, name='coaches')
]