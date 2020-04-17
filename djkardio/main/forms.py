from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Doctor, Patient, User


class PatientSignUpForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )
    pesel = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.pesel = self.cleaned_data.get('pesel')
        return user


class DoctorSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        return user