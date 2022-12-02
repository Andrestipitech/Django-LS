from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.persona.forms import PersonaFrom
from apps.persona.models import Persona
def saludoP(request):
    return render(request, 'persona/index.html')

def persona_view(request):
    if request.method == 'POST':
        form = PersonaFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('persona:index')
    else:
        form = PersonaFrom()
    return render(request, 'persona/indexp.html', {'form': form})

def persona_list(request):
    persona = Persona.objects.all()
    contexto ={'personas': persona}
    return render(request, 'persona/tables_persona.html', contexto)