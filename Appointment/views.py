from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Doctor, Patient, Appointment, Admin
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, AdminSerializer

# Create your views here.

@api_view(['GET'])
def home(request):
    return Response("Please go to dedicated endpoints for respective functionality.")

# ------------------------------- Doctor -------------------------------- #
# ----------------------------------------------------------------------- #

@api_view(['POST'])
def auth_doctor(request):
    
    try:
        # get all the data from the Doctor model
        username = request.data['username']
        password = request.data['password']

        if Doctor.objects.filter(username=username, password=password).exists():
            print("--------------------Authentication successful-----------------------")
            return Response({'message': 'Valid credentials', "is": True, "username": username})
        
        else:
            return Response({'error': 'Invalid credentials', "is": False})
        
    except:
        return Response({'error': 'Please try again later.', "is": False})


@api_view(['GET'])
def list_of_doctors(request):
    try:
        # get all the data from the Doctor model
        doctor = Doctor.objects.all()
        # serialize the data
        serializer = DoctorSerializer(doctor, many=True)
        # return the data in json format
        return Response(serializer.data)
    
    except:
        return Response({'error': 'Please try again later.', "is": False})


@api_view(['POST'])
def add_doctor(request):

    try:
        if Doctor.objects.filter(email=request.data['email']).exists():
            return Response({'error': 'Doctor already exists'})

        # serialize the data
        serializer = DoctorSerializer(data=request.data)

        # if the data is valid
        if serializer.is_valid():
            # save the data
            serializer.save()
        # return the data in json format
        return Response(serializer.data)
    
    except:
        return Response({'error': 'Please try again later.', "is": False})


@api_view(['PATCH', 'PUT'])
def update_doctor(request, pk):
    # get the data from the Doctor model
    try:
        doctor = Doctor.objects.get(id=pk)
    except:
        return JsonResponse({'error': 'Doctor does not exist'}, safe=False)
    # serialize the data
    serializer = DoctorSerializer(instance=doctor, data=request.data, partial=True)
    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    # return the data in json format
    return Response(serializer.data)


@api_view(['GET','DELETE'])
def delete_doctor(request, pk):
    # get the data from the Appointment model
    try:
        if request.method == "DELETE":
            doctor = Doctor.objects.get(id=pk)
            # delete the data
            doctor.delete()
            
            return Response('Doctor Deleted')
        
        else:
            doctor = Doctor.objects.get(id=pk)

            serializer = DoctorSerializer(instance=doctor, data=request.data, partial=True)

            if serializer.is_valid():
                return Response(serializer.data)
            
    except:
        # return the data in json format
        return JsonResponse({'error': 'Doctor does not exist'}, safe=False)


@api_view(['GET'])
def get_all_appointment_by_doctor_username(request, username):

    try:
        doctor = get_doctor_by_username(username)
        # print("doctor",doctor)
        # get the data from the Appointment model
        appointment = Appointment.objects.filter(doctor_id=doctor['id'])
        # serialize the data
        serializer = AppointmentSerializer(appointment, many=True)
        # return the data in json format
        return Response(serializer.data)
    
    except:
        return Response({'error': 'No Appointments', "is": False})
    



# ------------------------------- Patient -------------------------------- #
# ----------------------------------------------------------------------- #


@ api_view(['POST'])
def auth_patient(request):

    try:
    # get all the data from the Admin model
        username = request.data['username']
        password = request.data['password']
        if Patient.objects.filter(username=username, password=password).exists():
            print("--------------------Authentication successful-----------------------")
            return Response({'message': 'Valid credentials', "is": True, "username": username})
        else:
            return Response({'error': 'Invalid credentials', "is": False})
        
    except:
        return Response({'error': 'Please try again later.', "is": False})


@api_view(['GET'])
def list_of_patients(request):
    try:
        # print(request.headers)
        patient = Patient.objects.all()
        # serialize the data
        serializer = PatientSerializer(patient, many=True)
        # return the data in json format
        return Response(serializer.data)

    except:
        return Response({'error': 'Please try again later.', "is": False})


@api_view(['POST'])
def add_patient(request):
    try:
        # serialize the data
        serializer = PatientSerializer(data=request.data)

        # check if the patient already exists
        if Patient.objects.filter(email=request.data['email']).exists() or Patient.objects.filter(username=request.data['username']).exists():
            return Response({'error': 'Patient already exists'})

        # if the data is valid
        if serializer.is_valid():
            print("inside")
            # save the data
            serializer.save()
        # return the data in json format

        return Response(serializer.data)
    
    except:
        return Response({'error': 'Please try again later.', "is": False})


@api_view(['PATCH', 'PUT'])
def update_patient(request, pk):
    # get the data from the Patient model
    try:
        patient = Patient.objects.get(id=pk)
    except:
        return JsonResponse({'error': 'Patient does not exist'}, safe=False)

    # serialize the data
    serializer = PatientSerializer(
        instance=patient, data=request.data, partial=True)
    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    # return the data in json format
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def delete_patient(request, pk):
    try:
        if request.method == "DELETE":
            patient = Patient.objects.get(id=pk)
            # delete the data
            patient.delete()
            
            return Response('Patient Deleted')
        
        else:
            patient = Patient.objects.get(id=pk)

            serializer = PatientSerializer(instance=patient, data=request.data, partial=True)

            if serializer.is_valid():
                return Response(serializer.data)
            
    except:
        # return the data in json format
        return JsonResponse({'error': 'Patient does not exist'}, safe=False)


@api_view(['GET'])
def get_all_appointment_by_patient_username(request, username):
    try:
        patient = get_patient_by_username(username)
        # print("patient",patient)
        # get the data from the Appointment model
        appointment = Appointment.objects.filter(patient_id=patient['id'])
        # serialize the data
        serializer = AppointmentSerializer(appointment, many=True)
        # return the data in json format
        return Response(serializer.data)
    except:
        return JsonResponse({'error': 'No APpointments'}, safe=False)



# ---------------------------------- Appointments ----------------------------- #
# ----------------------------------------------------------------------------- #

@api_view(['GET'])
def list_of_appointments(request):
    try:
        # get all the data from the Appointment model
        appointment = Appointment.objects.all()
        # serialize the data
        serializer = AppointmentSerializer(appointment, many=True)

        n = len(serializer.data)

        for i in range(n):
            doctor_data = get_doctor_by_id(serializer.data[i]['doctor'])
            doctor_fullname = doctor_data['fullname']
            serializer.data[i]['doctor_fullname'] = doctor_fullname

            patient_data = get_patient_by_id(serializer.data[i]['patient'])
            patient_fullname = patient_data['fullname']
            serializer.data[i]['patient_fullname'] = patient_fullname

        return Response(serializer.data)
    
    except:
        return Response({'error': 'No Appointments', "is": False})


#  TO DO validate the appointment
@api_view(['POST'])
def add_appointment(request):

    try:
        if Doctor.objects.filter(id=request.data['doctor']).exists() == False:
            return JsonResponse({'error': 'Doctor does not exist'}, safe=False)

        if Patient.objects.filter(id=request.data['patient']).exists() == False:
            return JsonResponse({'error': 'Patient does not exist'}, safe=False)

        if Appointment.objects.filter(patient=request.data['patient'], doctor=request.data['doctor'], date=request.data['date'], time=request.data['time']).exists():
            return JsonResponse({'error': 'Appointment already exists'}, safe=False)

        # serialize the data
        serializer = AppointmentSerializer(data=request.data)

        # if the data is valid
        if serializer.is_valid():
            # save the data
            serializer.save()
        # return the data in json format
        return Response(serializer.data)
    
    except:
        return Response({'error': 'Please try again later.', "is": False})


# TO DO validate the appointment
@api_view(['PATCH', 'PUT'])
def update_appointment(request, pk):
    # get the data from the Appointment model
    try:
        appointment = Appointment.objects.get(id=pk)
    except:
        return JsonResponse({'error': 'Appointment does not exist'}, safe=False)

    # serialize the data
    serializer = AppointmentSerializer(
        instance=appointment, data=request.data, partial=True)
    # if the data is valid
    if serializer.is_valid():
        # save the data
        serializer.save()
    else:
        return JsonResponse(serializer.errors, safe=False)
    # return the data in json format
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def delete_appointment(request, pk):
    try:
        appointment = Appointment.objects.get(id=pk)
        if request.method == "DELETE":
            # delete the data
            appointment.delete()
            
            return Response('Appointment Deleted')
        
        else:
            serializer = AppointmentSerializer(instance=appointment, data=request.data, partial=True)

            if serializer.is_valid():
                return Response(serializer.data)
            
    except:
        # return the data in json format
        return JsonResponse({'error': 'Appointment does not exist'}, safe=False)



# -------------------------------- Admins -------------------------------- #
# ------------------------------------------------------------------------ #


@api_view(['GET'])
def list_of_admins(request):
    try:
        # get all the data from the Admin model
        admin = Admin.objects.all()
        # serialize the data
        serializer = AdminSerializer(admin, many=True)
        # return the data in json format
        return Response(serializer.data)
    except:
        return Response({'error': 'Please try again later.', "is": False})


@ api_view(['POST'])
def auth_admin(request):
    try:
        # get all the data from the Admin model
        username = request.data['username']
        password = request.data['password']
        if Admin.objects.filter(username=username, password=password).exists():
            print("--------------------Authentication successful-----------------------")
            return Response({'message': 'Valid credentials', "is": True, "username": username})
        else:
            return Response({'error': 'Invalid credentials', "is": False})

    except:
        return Response({'error': 'Please try again later.', "is": False})


@ api_view(['POST'])
def add_admin(request):
    try:
        # serialize the data
        serializer = AdminSerializer(data=request.data)

        if Admin.objects.filter(username=request.data['username']).exists():
            return Response({'error': 'Admin already exists'})

        # if the data is valid
        if serializer.is_valid():
            # save the data
            serializer.save()
        # return the data in json format
        return Response(serializer.data)
    
    except:
        return Response({'error': 'Please try again later.', "is": False})


@ api_view(['PATCH', 'PUT'])
def update_admin(request, pk):
    try:
        # get the data from the Admin model
        admin = Admin.objects.get(id=pk)
        # serialize the data
        serializer = AdminSerializer(instance=admin, data=request.data)
        # if the data is valid
        if serializer.is_valid():
            # save the data
            serializer.save()
        # return the data in json format
        return Response(serializer.data)
    
    except:
        return Response({'error': 'Please try again later.', "is": False})



# ------------------------------ Utility Functions -------------------------- #
# --------------------------------------------------------------------------- #

def get_doctor_by_id(pk):
    # get the data from the Doctor model
    doctor = Doctor.objects.get(id=pk)
    # serialize the data
    serializer = DoctorSerializer(doctor, many=False)
    # return the data in json format
    return serializer.data


def get_patient_by_id(pk):
    # get the data from the Patient model
    patient = Patient.objects.get(id=pk)
    # serialize the data
    serializer = PatientSerializer(patient, many=False)
    # return the data in json format
    return serializer.data




def get_patient_by_username(username):
    try:
        patient = Patient.objects.get(username=username)
        serializer = PatientSerializer(patient, many=False)
        # return the data in json format
        return (serializer.data)
    except:
        return ('Patient does not exist')
    

def get_doctor_by_username(username):
    try:
        doctor = Doctor.objects.get(username=username)
        serializer = DoctorSerializer(doctor, many=False)
        # return the data in json format
        return (serializer.data)
    except:
        return ('Doctor does not exist')