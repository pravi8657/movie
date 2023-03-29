from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import movieform
from .models import table
from django.views.generic import ListView  # class based generic views
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
def index(request):
    return HttpResponse('hello')

def functionname(request):
    na = 'he'
    return render(request, 'new.html', {'m': na})


def movie(request):
    ml = table.objects.all()
    return render(request, 'new.html', {'keyvalue': ml})


def detail(request, id):
    o = table.objects.get(id=id)
    return render(request, 'detail.html', {'okk': o})


# function for form
def addmovie(request):
    # post method to get data from form
    if request.method == 'POST':
        # insert it into table
        k = request.POST.get('name', )
        p = request.POST.get('year', )
        e = request.POST.get('description', )
        y = request.FILES['image']

        # redirected to homepage
        t = table(name=k, date=p, about=e, image=y)

        # save
        t.save()
        return redirect('movieapp:2')

    return render(request, 'addmovie.html')


def update(request, id):
    p = table.objects.get(id=id)
    g = movieform(request.POST or None, request.FILES, instance=p)
    if g.is_valid():
        g.save()
        return redirect('movieapp:2')
    else:
        form = movieform(instance=p)
    return render(request, 'update.html', {'ll': p, 'k': form})


# delete
def delete(request, id):
    if request.method == "POST":
        d = table.objects.get(id=id)
        d.delete()
        return redirect('movieapp:2')
    return render(request, "delete.html")


# class based generic views
class movielistview(ListView):
    model = table
    template_name = 'new.html'
    context_object_name = 'keyvalue'


# detail view
class moviedetailview(DetailView):
    model = table
    template_name = 'detail.html'
    context_object_name = 'okk'

#update view
class movieupdateview(UpdateView):
    model = table
    template_name = 'edit.html'
    context_object_name = 'form'
    fields = ['name', 'image', 'date', 'about']

    def get_success_url(self):  # return redirect
        return reverse_lazy('movieapp:cbvdetail', kwargs={'pk': self.object.id})

class moviedeleteview(DeleteView):
    model = table
    template_name ='delete.html'
    success_url=reverse_lazy('movieapp:cbvhome')

