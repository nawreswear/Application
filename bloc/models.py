from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    description=models.TextField(default='Non définie')
    DOMAIN_CHOICES=[('CHG','Charte graphique'),
    ('O3D','Objet 3D'),
    ('SCE','Scénarisation'),
    ]
    type=models.CharField(max_length=3,choices=DOMAIN_CHOICES,default='CHG')
from datetime import date
from django.core.validators import MaxValueValidator
from django.utils import timezone

class Project(models.Model):
    libellai=models.CharField(max_length=100,default='')
    TYPE_CHOICES=[('O','On cours '),('N','Non')]
    achevé=models.CharField(max_length=1,choices=TYPE_CHOICES,default='O')
    description = models.TextField(default=' ')
    services = models.ManyToManyField('Service',through='Detail')
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    pourcentage=models.IntegerField(default=0)
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    image =models.ImageField(upload_to='portfolio_images')
class Detail(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_files/')

class Team(models.Model):
    name = models.CharField(max_length=100,default=' ')
    personnel = models.ManyToManyField('Personnel')

class Personnel(models.Model):
    name = models.CharField(max_length=100,default=' ')
    prenom=models.CharField(max_length=100,default=' ')
    lien_profil = models.URLField(blank=True)
    expertise = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ManyToManyField('Project')

class Testimonial(models.Model):
    project = models.ForeignKey('Project',on_delete=models.CASCADE)
    content = models.TextField(default=' ')
    author = models.CharField(max_length=100,default=' ')

class Contact(models.Model):
    name = models.CharField(max_length=100,default=' ')
    email = models.EmailField(default=' ')
    phone = models.CharField(max_length=20,default=' ')
    message = models.TextField(default=' ')

class Tache(models.Model):
    nom = models.CharField(max_length=100,default=' ')
    description = models.TextField(default='Non définie')
    personne = models.ForeignKey('Personnel', on_delete=models.CASCADE,null=True, blank=True)
    projet = models.ForeignKey('Project', on_delete=models.CASCADE)
    date_depot = models.DateField(null=True, blank=True)    
    Img = models.ImageField(upload_to='media/', null=True, blank=True)
    def __str__(self):
        return (self.nom +","+self.description)
# Create your models here.
