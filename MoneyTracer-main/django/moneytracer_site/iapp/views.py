from django.shortcuts import render, redirect
from .models import Person, Expenses, Income
from .forms import ExpensesForm


def iapp_home(request):
    iapp = Expenses.objects.order_by('-date')
    return render(request, 'main/iapp_home.html', {'iapp': iapp})


def create(request):
    form = ExpensesForm()
    error = ''
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'ERROR'

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/create.html', )