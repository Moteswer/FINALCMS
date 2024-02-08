from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Staff, Admin, Doctor, Login, Patient, Role
from .serializers import SignupSerializer, LoginSerializer, StaffSerializer, DoctorSerializer, PatientSerializer, \
    RoleSerializer, SpecializationSerializer, EmailSerializer


def populate_login_table():
    # Get data from Staff table
    staff_data = Staff.objects.values('email', 'password')

    # Get data from Admin table
    admin_data = Admin.objects.values('username', 'password')

    # Get data from Doctor table
    doctor_data = Doctor.objects.values('email', 'password')

    # Create Login objects from the collected data
    for data in staff_data:
        Login.objects.create(email=data['email'], password=data['password'])

    for data in admin_data:
        Login.objects.create(email=data['username'], password=data['password'])

    for data in doctor_data:
        Login.objects.create(email=data['email'], password=data['password'])


@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        # Create a new Login object
        Login.objects.create(email=email, password=password,role=role)

        return Response({'message': 'Signup successful'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        email = data.get('email')
        password = data.get('password')

        # Check if the email and password match in any of the tables
        user = None
        for model in [Staff, Admin, Doctor]:
            user = model.objects.filter(email=email, password=password).first()
            if user:
                if isinstance(user, Staff) or isinstance(user, Admin):
                    role_details = RoleSerializer(user.role).data  # Serialize role details
                    return Response({'message': 'Login successful', 'role_details': role_details},
                                    status=status.HTTP_200_OK)
                elif isinstance(user, Doctor):
                    specialization_details = SpecializationSerializer(user.specialization).data
                    return Response({'message': 'Login successful', 'specialization_details': specialization_details},
                                    status=status.HTTP_200_OK)

        # If user is not found
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

    # If request data is not valid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def login_list(request):
    if request.method == 'GET':
        logins = Login.objects.all()
        login_data = []
        for login in logins:
            role_serializer = RoleSerializer(login.role)
            login_info = {
                'id': login.id,
                'email': login.email,
                'password': login.password,
                'role': role_serializer.data
            }
            login_data.append(login_info)
        return Response(login_data)



@api_view(['GET', 'POST'])
def staff_list(request):
    if request.method == 'GET':
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleList(APIView):
    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def staff_detail(request, pk):
    try:
        staff = Staff.objects.get(pk=pk)
    except Staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StaffSerializer(staff)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def doctor_detail(request, pk):
    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def patient_list(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_doctors_by_specialization_id(request, specialization_id):
    try:
        doctors = Doctor.objects.filter(specialization=specialization_id)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Doctor.DoesNotExist:
        return Response({"error": "Doctors with the specified specialization ID do not exist"}, status=status.HTTP_404_NOT_FOUND)



# views.py
from django.http import JsonResponse
from .models import Staff

def get_emails(request):
    emails = Staff.objects.values_list('email', flat=True)
    return JsonResponse({'emails': list(emails)})

class CheckEmailAPIView(APIView):
    def post(self, request):
        # Deserialize the request data using the EmailSerializer
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if Staff.objects.filter(email=email).exists():
                return Response({'exists': True})
            else:
                return Response({'exists': False})
        else:
            # Return error response if serializer data is invalid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def check_email_exists(request):
    email = request.GET.get('email')
    if email:
        email_exists = Staff.objects.filter(email=email).exists()
        return Response(email_exists)
    else:
        return Response(False)

@api_view(['GET'])
def check_phone_number_exists(request):
    phone_number = request.GET.get('phone_number')
    if phone_number:
        phone_number_exists = Staff.objects.filter(phone_number=phone_number).exists()
        return Response(phone_number_exists)
    else:
        return Response(False)



