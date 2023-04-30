# write a serializer for the model
from rest_framework import serializers
from .models import Admin, Doctor, Patient, Appointment


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        # fields = '__all__'
        fields = ['id', 'username', 'fullname', 'email', 'password', 'phone',
                  'address', 'specialization', 'fees']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        # fields = ('id', 'name', 'email', 'gender',  'password', 'phone',
        #         'address', 'age')


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        # fields = '__all__'
        fields = ('id', 'doctor', 'patient', 'date', 'time', 'status', 'description')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        # fields = ('id', 'username', 'password')
