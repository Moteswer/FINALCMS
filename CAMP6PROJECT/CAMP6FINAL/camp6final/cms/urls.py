from django.urls import path

from . import views
from .views import signup, login, staff_detail, staff_list, doctor_detail, doctor_list, patient_list, patient_detail, \
    login_list, RoleList, get_emails, CheckEmailAPIView, check_email_exists

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('login2/', login_list, name='login-list'),
    path('staffs/', staff_list),
    path('staffs/<int:pk>/', staff_detail),
    path('doctors/', doctor_list),
    path('doctors/<int:pk>/', doctor_detail),
    path('patients/', patient_list),
    path('patients/<int:pk>/', patient_detail),
    path('specialization/<int:specialization_id>/', views.get_doctors_by_specialization_id, name='get_doctors_by_specialization'),
    path('roles/', RoleList.as_view(), name='role-list'),
    # path('api/check-email/', check_email, name='check_email'),
    path('api/get-emails/', get_emails, name='get_emails'),
    path('check-email/', CheckEmailAPIView.as_view(), name='check_email'),
    path('api/check-email', check_email_exists, name='check_email_exists_in_staff_table'),
    path('api/check-phone-number', views.check_phone_number_exists, name='check_phone_number_exists'),
]


