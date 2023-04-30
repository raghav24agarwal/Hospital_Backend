from django.db import models

# Create your models here.

class Admin(models.Model):
    username = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username
    

class Doctor(models.Model):
    username = models.CharField(max_length=100, null=False)
    fullname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=100, blank=True)
    fees = models.IntegerField(default=200)

    def __str__(self):
        return self.fullname
    

class Patient(models.Model):
    username = models.CharField(max_length=100, null=False)
    fullname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    age = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.fullname
    

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100, default="New", blank=True)
    description = models.CharField(max_length=2000, default='New Appointment', blank=True)

    def __str__(self):
        return "Patient " + self.patient.fullname + " scheduled an appointment with Doctor " + self.doctor.fullname
