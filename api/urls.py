from django.urls import path

from . import views

urlpatterns = [
    path("student/",views.view_student,name="student")
]
