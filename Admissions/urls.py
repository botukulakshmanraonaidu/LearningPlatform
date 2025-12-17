from django.urls import path
from Admissions.views import AddAdmission,addadmissionread,readaddedrow,updaterecord,deleterecord
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('addadmission/',login_required(AddAdmission.as_view())),
    path('readadmissions/',login_required(addadmissionread.as_view()),name='readadmissions'),
    path('readaddedrow/<int:pk>',login_required(readaddedrow.as_view()),name='readrow'),
    path('updaterecord/<int:pk>',login_required(updaterecord.as_view()),name='updaterecord'),
    path('deleterecord/<int:pk>',login_required(deleterecord.as_view())),
]
