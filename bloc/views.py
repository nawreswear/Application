from django.http import HttpResponse ,HttpResponseRedirect
from django.template import loader
from .models import Detail
from .models import Project
from .models import Personnel
from .models import Service
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Team
from .models import Tache
from .forms import DetailForm
from .forms import ServiceForm
from .forms import ProjectForm,ContactForm
from .forms import TeamForm,UserRegistrationForm
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .models import Testimonial
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Detail
from django.contrib import messages
from django.contrib.auth import authenticate ,login  , logout 
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.urls import reverse

def liste_tache(self):
    taches = Tache.objects.filter(projet=self)
    total_taches = taches.count()
    taches_terminees = taches.filter(etat_avancement__nom='Terminé').count()
    pourcentage = (taches_terminees / total_taches) * 100 if total_taches > 0 else 0
    self.etat_avancement.pourcentage = pourcentage
    self.etat_avancement.save()
    return pourcentage

@login_required # Décorateur pour s'assurer que l'utilisateur est connecté
def user(request):
    # Récupérer les informations de l'utilisateur connecté
    user = request.user
    # Passer les informations de l'utilisateur au contexte pour les utiliser dans le template
    context = {'user': user}
    # Rendre le template 'user_profile.html' avec le contexte pour générer la page HTML
    return render(request, 'magasin/user.html', context)
class DetailCreate(CreateView):
    model = Detail
    fields = ['name', 'description', 'price', 'file', 'projet', 'service']

class DetailUpdate(UpdateView):
    model = Detail
    fields = ['name', 'description', 'price', 'file', 'projet', 'service']

class DetailDelete(DeleteView):
    model = Detail
    success_url = reverse_lazy('detail_list')
from .models import Personnel
from .models import Personnel
from .forms import PersonnelForm

def liste_personnel(request):
    personnel = Personnel.objects.all()
    context = {'personnel': personnel}
    return render(request, 'bloc/liste_personnel.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Project

'''def detail_projet(request, project_id):
    # Retrieve the project using project_id or return a 404 error if not found
    project = get_object_or_404(Project, pk=project_id)

    # Pass the project object to the template for rendering
    context = {'project': project}
    return render(request, 'bloc/detailprojet.html', context)'''


def ajouter_personne(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bloc:liste_personnel')  
    else:
        form = PersonnelForm()
    context = {'form': form}
    return render(request, 'bloc/ajouter_personne.html', context)
def detail_form(request):
    details = Detail.objects.all()
    return render(request, 'bloc/detail_form.html', {'details': details})

def Equipe(request):
    membres = Team.objects.all()
    if request.method == "POST" : 
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bloc:Equipe')
    else :
        form = TeamForm() #créer formulaire vide
    return render(request,'bloc/Equipe.html',{'form':form, 'membres': membres})

def deleteequipe(request,name): 
    try:
        form = Team.objects.get(name=name)  
        form.delete()
    except Team.MultipleObjectsReturned:
        equipe = Team.objects.filter(name=name)
    except Team.DoesNotExist:
        pass
    return redirect('bloc/detailequipe.html')
def index(request):
    return render(request,'bloc/home.html')

def detailequipe(request,nom):
    equipe = Team.objects.get(nom=nom) 
    return render(request,'bloc/detailequipe.html', context={'equipe':equipe}) 
    
def ldetail(request):
    details = Detail.objects.all()
    return render(request, 'bloc/ldetail.html', {'details': details})

def add_detail(request, pk):
    detail = get_object_or_404(Detail, pk=pk)
    return render(request, 'bloc/detail.html', {'detail': detail})

def portfolio(request):
    projets= Project.objects.all()
    context={'projets':projets}
    return render(request,'bloc/portfolio.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('bloc:contact') Redirection ou affichage d'un message de succès
    else:
        form = ContactForm()
    return render(request, 'bloc/contact.html', {'form': form})

def meProject(request):
    context = {}
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('bloc:lmeProject')
            except:
                pass
    else:
        form = ProjectForm()
        context.update({'form':form}) 
    return render(request,'bloc/meProject.html',context)

def detailprojet(request, libellai):
    projets = get_object_or_404(Project,libellai=libellai) 
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=projets) 
        if form.is_valid():
            form.save()
            return redirect(reverse('bloc:lmeProject'))
    else:
        form = ProjectForm(instance=projets)
    context = {'form': form, 'projets': projets}        
    return render(request,'bloc/detail_projet.html',context)


def lmeProject(request):
    projets = Project.objects.all()  
    context={'projets': projets}
    return render(request,'bloc/lmeProject.html',context) 
    
from django.shortcuts import render, get_object_or_404
from .models import Project
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Project


    
def deleteprojet(request,libellai):
    projets = Project.objects.filter(libellai=libellai)
    
    for projet in projets:
        # Supprimer le projet ou prendre d'autres mesures nécessaires
        projet.delete()
    return redirect('bloc:lmeProject')

def projets_realises(request):
    projets = Project.objects.filter(achevé='N')
    return render(request,'bloc/projets_realises.html', {'projets': projets})

def deleteservice(request,description):
    service = Service.objects.get(description=description)  
    service.delete()
    return redirect('bloc:service_detail')

def projets_en_cours(request):
    projets = Project.objects.filter( achevé='O')
    return render(request,'bloc/projets_en_cours.html', {'projets': projets})

def deleteprojets_realises(request,libellai):
    projets = Project.objects.get(libellai=libellai)  
    projets.delete()
    
    return redirect('bloc:projets_realises')

def deleteprojets_realises(request, libellai):
    projets = Project.objects.filter(libellai=libellai)
    
    if projets.exists():
        projets.delete()
        return redirect('bloc:projets_realises')
    else:
        # Gérer le cas où aucun projet n'est trouvé
        return HttpResponse("Aucun projet trouvé.")

def deleteequipe(request,name): 
    try:
        form = Team.objects.get(name=name)  
        form.delete()
    except Team.MultipleObjectsReturned:
        equipe = Team.objects.filter(name=name)
    except Team.DoesNotExist:
        pass
    return redirect('bloc:Equipe_details')


def detailequipe(request,name):
    equipe = Team.objects.get(name=name) 
    return render(request,'bloc/detailequipe.html', context={'equipe':equipe}) 

def deleteservice(request, description):
    services = Service.objects.filter(description=description)
    
    if services.exists():
        services.delete()
        return redirect('bloc:service_detail')
    else:
        # Gérer le cas où aucun service n'est trouvé
        return HttpResponse("Aucun service trouvé.")
    
def Equipe_details(request):
    membres = Team.objects.all()
    context = {'membres':membres}
    return render(request,'bloc/Equipe_details.html',context)

def Services(request):
    if request.method=='POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('bloc:Services')
            except:
                pass
    else:        
        form = ServiceForm()  
    return render(request,'bloc/Services.html',context = {'form':form}  )
 
def service_detail(request):
    try:
        service = Service.objects.all()  
        context={'service':service}
    except Question.DoesNotExist:
        raise Http404("service detail does not exist")
    return render(request,'bloc/service_detail.html',context) 

from django.utils.text import slugify
from django.shortcuts import get_object_or_404, reverse, redirect
from .models import Service
from .forms import ServiceForm

def service_update(request, description):
    service = get_object_or_404(Service,description=description) 
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service) 
        if form.is_valid():
            form.save()
            return redirect(reverse('bloc:service_detail'))
    else:
        form = ServiceForm(instance=service)
    context = {'form': form, 'service': service}        
    return render(request,'bloc/service_update.html',context)

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bloc:service_detail')
    else:
        form = ServiceForm()
    return render(request,'bloc/service_form.html',{'form': form})

def deleteprojets_en_cours(request,libellai):
    projets = Project.objects.filter(libellai=libellai)
    
    if projets.exists():
        projets.delete()
        return redirect('bloc:projets_en_cours')
    else:
        # Gérer le cas où aucun projet n'est trouvé
        return HttpResponse("Aucun projet trouvé.")
    
def portfolio(request):
    projects = Project.objects.filter(achevé='N')
    return render(request,'bloc/portfolio.html', {'projects': projects})


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bloc:lmeProject')
    else:
        form = ServiceForm()
    return render(request, 'bloc/meProject.html', {'form': form})

def Equipe_details(request):
    membres = Team.objects.all()
    context = {'membres': membres}
    return render(request,'bloc/Equipe_details.html',context)

'''def user_projects(request):
    user = request.user 
    # récupérer l'utilisateur connecté
    projects = Projet.objects.filter(user=user) 
    # récupérer les projets créés par l'utilisateur connecté
    return render(request, 'bloc/user_projects.html', {'projects': projects})'''

'''def user_project_details(request, project_id):
    user = request.user
     # récupérer l'utilisateur connecté
    project = Projet.objects.get(id=project_id, user=user)
     # récupérer le projet correspondant à l'ID fourni dans l'URL et créé par l'utilisateur connecté
    return render(request, 'bloc/user_project_details.html', {'project': project})'''
def index(request):
    return render(request,'bloc/home.html')

from .forms import UserCreationForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('bloc:base')#home
    else :
        form = UserCreationForm()
    return render(request,'bloc/registration/register.html',{'form': form})
# Create your views here.
