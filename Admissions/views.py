from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from Admissions.models import addadmissions
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

class AddAdmission(PermissionRequiredMixin,CreateView):
    model = addadmissions
    fields = ('__all__')
    template_name = 'Admissions/add-admission.html'
    # success_url = reverse_lazy('readrow')
    permission_required = 'Admissions.add_addadmissions'

class addadmissionread(PermissionRequiredMixin,ListView):
    model = addadmissions
    template_name = 'Admissions/admission-report.html'
    context_object_name = 'objects'
    permission_required = 'Admissions.view_addadmissions'

class readaddedrow(PermissionRequiredMixin,DetailView):
    model = addadmissions
    template_name = 'Admissions/readnewdata.html'
    # context_object_name = 'objects'
    permission_required = 'Admissions.view_addadmissions'

class updaterecord(PermissionRequiredMixin,UpdateView):
    model = addadmissions
    fields = ('student_name','father_name','dob','course_opted')
    template_name = 'Admissions/add-admission.html'
    success_url = reverse_lazy('readadmissions')
    permission_required = 'Admissions.change_addadmissions'

class deleterecord(PermissionRequiredMixin,DeleteView):
    model = addadmissions
    template_name = 'Admissions/delete_confirm.html'
    success_url = reverse_lazy('readadmissions')
    permission_required = 'Admissions.delete_addadmissions'
