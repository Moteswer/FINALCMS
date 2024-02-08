from django.contrib import admin

from .models import Role, Admin, Staff, Doctor, Patient, Appointment, Specialization

admin.site.register(Role)
admin.site.register(Admin)
admin.site.register(Staff)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Specialization)
# Register your models here.
