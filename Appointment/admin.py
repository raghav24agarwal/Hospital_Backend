from django.contrib import admin
from .models import Admin, Doctor, Patient, Appointment

# Register your models here.
admin.site.register({Admin, Doctor, Patient, Appointment})
