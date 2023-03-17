from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, Usersinfo, MessageForm, DemandeSolutionForm
from django.core import serializers
from datetime import datetime
from .models import Solutions, demandesolution, Message


# Create your views here.

def test(request):
    return render (request,'sticweb/test.html')
def index(request):
    solutions = Solutions.objects.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = MessageForm()
    context = {'solutions': solutions, 'form': form}
    return render(request,'sticweb/index.html', context)

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm()
    return render(request, 'sticweb/contact.html', {'form': form})

def solutions(request):
        solutions = Solutions.objects.all()
        return render(request, 'sticweb/solutions.html', {'solutions': solutions})

def DetailSolution(request, Solutions_id):
    #solutions = Solutions.objects.all()
    solutions = get_object_or_404(Solutions, id=Solutions_id)
    numero = None
    mon_user = None  # initialisation de mon_user en dehors de la condition if
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form1 = DemandeSolutionForm(request.POST)

        #if form.is_valid():
        if not form.is_valid():
            print("voici le prob ", form.errors)
        else:
            mon_user = form.save(commit=False)
            numero = mon_user.tel
        if not form1.is_valid():
            print("voici le prob2 ", form1.errors)
        else:
            demande = form1.save(commit=False)

        print("num", numero)
        existe_deja = Usersinfo.objects.filter(tel=numero).exists()
        print("existe : ", existe_deja)

        if existe_deja:
            # Le numéro existe déjà dans la base de données, récupérer l'ID de Solutions et enregistrer demandesolution dans la base
            mon_user = Usersinfo.objects.get(tel=numero)
            # demande.save()
           # if form1.is_valid():
            #demande = form1.save(commit=False)
            demande.datedemande = datetime.today()
            demande.demandeur_id = mon_user
            demande.solutiondemande_id = solutions
            demande.save()
        else:
            # Le numéro n'existe pas dans la base de données, enregistrer le numéro et le post
            # mon_user.save()  # vous devez indenter cette ligne ici
            form.save()
            # demande = form1.save(commit=False)
            demande.datedemande = datetime.today()
            demande.demandeur_id = mon_user
            demande.solutiondemande_id = solutions
            demande.save()
        return redirect('solution')
    else:
        form = ContactForm()
        form1 = DemandeSolutionForm()
        context = {'solutions': solutions, 'form': form, 'form1': form1}
    return render(request, 'sticweb/DetailSolution.html', context)

def foolio(request):
    return render(request, 'sticweb/foolio.html')

def services(request):
    return render(request, 'sticweb/services.html')

def api_listeUsers(request):
    User = Usersinfo.objects.all()
    json = serializers.serialize("json", User)
    return HttpResponse(json)

def api_listeMessage(request):
    message = Message.objects.all()
    json = serializers.serialize("json", message)
    return HttpResponse(json)