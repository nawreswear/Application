from django.forms import ModelForm
from django import forms
from .models import Detail
from .models import Service
from .models import Project 
from .models import Contact
from .models import Team,Testimonial
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Personnel
class DetailForm(ModelForm):
    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    file = forms.FileField()
    class Meta:
        model = Detail
        fields = "__all__" 
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = "__all__"
class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = "__all__"
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields =   "__all__"

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = "__all__"
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')