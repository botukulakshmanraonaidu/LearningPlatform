from django.urls import path
from classes import views as cls
from classes.views import DownloadPythonStudentsPDF


urlpatterns = [ 
    path('pythonprog/<str:course_name>/',cls.python_students,name='python_students'),
    path('pythonpdf/<str:course_name>/',DownloadPythonStudentsPDF.as_view(),name='download_python_pdf'),
    path('javaprog/<str:course_name>/',cls.java_students,name='java_students'),
    path('dot-net/<str:course_name>',cls.dot_net_students,name='dot-net_students'),
    path('C&C++/<str:course_name>',cls.CandCplusstudents,name='C&C++_students'),
]