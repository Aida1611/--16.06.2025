from django import forms
from .models import Project, Programmer, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


class ProgrammerForm(forms.ModelForm):
    class Meta:
        model = Programmer
        fields = ['name', 'age', 'group']  # Только эти поля, без user


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
