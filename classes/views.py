from django.shortcuts import render
from Admissions.models import addadmissions
# from django.http import HttpResponse
# Create your views here.
from django.views.generic import View
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse


def python_students(request,course_name):
    student = addadmissions.objects.filter(course_opted__iexact=course_name) # incase-sensive for better filter
    context = {'student':student}
    return render(request,'classes/python-programming.html',context)

class DownloadPythonStudentsPDF(View):

    def get(self, request, course_name):
        students = addadmissions.objects.filter(course_opted__iexact=course_name)

        template_path = 'classes/python-programming.html'
        context = {'student': students}

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="python_students.pdf"'

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse("PDF generation failed")

        return response


def java_students(request,course_name):
    student = addadmissions.objects.filter(course_opted__iexact=course_name)
    context = {'student':student}
    return render(request,'classes/java-programming.html',context)

def dot_net_students(request,course_name):
    student = addadmissions.objects.filter(course_opted__iexact=course_name) # by default django accept case-sentive
    context = {'student':student}
    return render(request,'classes/dot-net.html',context)

def CandCplusstudents(request,course_name):
    student = addadmissions.objects.filter(course_opted__iexact=course_name) # by default django accept case-sentive
    context = {'student':student}
    return render(request,'classes/CandCplus.html',context)