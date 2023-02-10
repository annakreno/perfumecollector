from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Perfume

# Create your views here.

def home(request):
    return render(request, 'home.html')

def perfumes_index(request):
  perfumes = Perfume.objects.all()
  return render(request, 'perfumes/index.html', { 'perfumes': perfumes})

def about(request):
  return render(request, 'about.html')

def perfumes_detail(request, perfume_id):
  perfume = Perfume.objects.get(id=perfume_id)
  return render(request, 'perfumes/detail.html', {'perfume': perfume})

class PerfumeCreate(CreateView):
  model = Perfume
  fields = "__all__"

class PerfumeUpdate(UpdateView):
  model = Perfume
  fields = "__all__"

class PerfumeDelete(DeleteView):
  model = Perfume
  success_url = '/perfumes'


