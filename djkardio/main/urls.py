from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from .views.patients import PatientSignUpView
from .views.doctors import DoctorSignUpView
from .views.views import home


urlpatterns = [
    path('', home, name='home'),
    path('patients', views.views.patients, name='patients'),
    path('home-patient', TemplateView.as_view(template_name='home_patient.html'), name='home_patient'),
    path('home-doctor', TemplateView.as_view(template_name='home_doctor.html'), name='home_doctor'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/signup/', main.SignUpView.as_view(), name='signup'),
    path('accounts/signup/patient/', PatientSignUpView.as_view(), name='patient_signup'),
    path('accounts/signup/doctor/', DoctorSignUpView.as_view(), name='doctor_signup'),
]