from django.shortcuts import render,redirect
from .forms import financialForm
from .models import Financial
# Create your views here.

def financial_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = financialForm()
        else:
            ids = Financial.objects.get(pk = id)
            form = financialForm(instance=ids)
        return render(request, "ethanai_register/form.html", {'form':form})
    else:
        if id == 0:
            form = financialForm(request.POST)
        else:
            ids = Financial.objects.get(pk = id)
            form = financialForm(request.POST,instance=ids)
        if form.is_valid():
            form.save()
        return redirect('/financial/list')

def financial_list(request):
    context = {'financial_list' : Financial.objects.all()}
    return render(request, "ethanai_register/list.html", context)

def financial_delete(request,id):
    ids = Financial.objects.get(pk = id)
    ids.delete()
    return redirect('/financial/list')