from django.db import models

# Create your models here.
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):

        return self.name


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=40, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False)


    def __str__(self):
        return self.first_name

class Admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True,default='')
    dateandtime = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


    def __str__(self):
        return self.username



class Specialization(models.Model):
    id = models.AutoField(primary_key=True)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.specialization



class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE,default='')
    gender = models.CharField(max_length=1, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    consultation_fee = models.IntegerField()
    Duty_time = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    height = models.CharField(max_length=3)
    weight = models.CharField(max_length=3)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    appointment_date = models.DateField(auto_now=True)
    appointment_time = models.TimeField(auto_now=True)
    token_no = models.CharField(max_length=10)


class Login(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)


    def __str__(self):
        return self.email

