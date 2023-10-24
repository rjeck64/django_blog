from django.shortcuts import render, redirect , get_object_or_404
from kategori.models import Category
from .forms import CreateKategori


# Create your views here.
def kategori(request):
    kategori = Category.objects.all()
    return render(request, 'kategori.html', {'category' : kategori})

def create(request):
    form = CreateKategori()
    return render(request, 'addkategori.html', {'form' : form})

def store(request):
    Category.objects.create(Category_name = request.POST.get('Category_name'))
    return redirect('kategori')

def deleteKategori(request,id):
    kategori = get_object_or_404(Category, id = id)
    kategori.delete()

    return redirect('kategori')

def editKategori(request,id):
    kategori = get_object_or_404(Category, id = id)
    form = CreateKategori(instance=kategori)
    return render(request, 'editkategori.html', {'form' : form , 'kategori' : kategori})

def updateKategori(request,id):
    kategori = get_object_or_404(Category, id = id)
    form = CreateKategori(request.POST , instance= kategori)
    form.save()
    return redirect("kategori")

