from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentFM
from .models import Student
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

# def addshow(request):
#     if request.method == 'POST':
#         fm = StudentFM(request.POST)
#         if fm.is_valid():
#             fm.save()
#             return HttpResponseRedirect('/')
#     else:
#         fm = StudentFM()
#     return render(request, 'enroll/addshow.html', {'form':fm, 'data':Student.objects.all()})

class StuCreView(CreateView):
    CreateView.form_class = StudentFM
    success_url = '/'

class StudentListView(ListView):
    model = Student


class StuDelView(DeleteView):
    model = Student
    success_url = '/show/'

class StuUpdView(UpdateView):
    model = Student
    form_class = StudentFM
    success_url = '/show/'

# def delete(request, id):
#     if request.method == 'POST':
#         Student.objects.get(pk=id).delete()
#         return HttpResponseRedirect('/')

# def update(request, id):
#     pi = Student.objects.get(pk=id)
#     if request.method == 'POST':
#         fm = StudentFM(request.POST, instance=pi)
#         fm.save()
#         return HttpResponseRedirect('/')
#     else:
#         fm = StudentFM(instance=pi)
#     return render(request, 'enroll/update.html', {'form':fm})