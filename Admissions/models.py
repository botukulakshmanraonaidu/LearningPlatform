from django.db import models
from django.urls import reverse

class addadmissions(models.Model):
    COURSE_CHOICES = [
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('C & C++', 'C & C++'),
        ('Dot-Net', 'Dot-Net'),
    ]
    student_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    dob = models.DateField()
    course_opted = models.CharField(max_length=50, choices=COURSE_CHOICES, default='Python')
    Registration_fee = models.IntegerField()

    def get_absolute_url(self):
        return reverse('readrow', kwargs={'pk': self.pk})
