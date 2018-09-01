from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm
from .models import Expense

# Create your views here.
@login_required
def add_ticket(request):
    form = ExpenseForm(request.POST or None)
    print(form)
    if form.is_valid():
        listOfUsers = form.cleaned_data['users']
        e = form.save(commit=False)
        e.added_by = request.user 
        e.kot = request.user.kot
        e.save()
        e.debit(listOfUsers)

    return render(request, 'bank/add_ticket.html', locals())
