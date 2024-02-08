from rest_framework import serializers

from .models import Login, Staff, Doctor, Patient, Role, Specialization


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['role', 'email', 'password']
    def create(self, validated_data):
        return validated_data



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'



class StaffSerializer(serializers.ModelSerializer):
    role_detail = RoleSerializer(source='role',read_only=True)
    class Meta:
        model = Staff
        fields = '__all__'





class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'specialization']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

