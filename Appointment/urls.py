from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    
    path('authDoctor', views.auth_doctor, name='auth_doctor'),
    path('allDoctors', views.list_of_doctors, name='list_of_doctors'),
    path('addDoctor', views.add_doctor, name='add_doctor'),
    path('updateDoctor/<int:pk>', views.update_doctor, name='update_doctor'),
    path('deleteDoctor/<int:pk>', views.delete_doctor, name='delete_doctor'),
    path('doctorAllAppointments/<str:username>', views.get_all_appointment_by_doctor_username, name="get_all_appointment_by_doctor_username"),

    path('authPatient', views.auth_patient, name='auth_patient'),
    path('allPatients', views.list_of_patients, name='list_of_patients'),
    path('addPatient', views.add_patient, name='add_patient'),
    path('updatePatient/<int:pk>', views.update_patient, name='update_patient'),
    path('deletePatient/<int:pk>', views.delete_patient, name='delete_patient'),
    path('patientAllAppointments/<str:username>', views.get_all_appointment_by_patient_username, name="get_all_appointment_by_patient_username"),

    path('allAppointments', views.list_of_appointments, name='list_of_appointment'),
    path('addAppointment', views.add_appointment, name='add_apoointment'),
    path('updateAppointment/<int:pk>', views.update_appointment, name='update_appointment'),
    path('deleteAppointment/<int:pk>', views.delete_appointment, name='delete_appointment'),

    path('allAdmins', views.list_of_admins, name='list_of_admins'),
    path('addAdmin', views.add_admin, name='add_admin'),
    path('updateAdmin/<int:pk>', views.update_admin, name='update_admin'),
    path('authAdmin', views.auth_admin, name='auth_admin')
]