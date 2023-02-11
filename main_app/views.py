from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Perfume
from .forms import ReviewForm

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
  review_form = ReviewForm()
  return render(request, 'perfumes/detail.html', {'perfume': perfume, 'review_form': review_form})

class PerfumeCreate(CreateView):
  model = Perfume
  fields = "__all__"

class PerfumeUpdate(UpdateView):
  model = Perfume
  fields = "__all__"

class PerfumeDelete(DeleteView):
  model = Perfume
  success_url = '/perfumes'

def add_review(request, perfume_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.perfume_id = perfume_id
    new_review.save()
  return redirect('detail', perfume_id=perfume_id)


