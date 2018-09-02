from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm
from .models import Expense, Transaction

# Create your views here.
@login_required
def add_ticket(request):
    form = ExpenseForm(request.POST or None)
    bank_page = 'active'
    print(request.user.get_transactions())
    if form.is_valid():
        listOfUsers = form.cleaned_data['users']
        e = form.save(commit=False)
        e.added_by = request.user 
        e.kot = request.user.kot
        e.save()
        e.debit(listOfUsers)
        if form.cleaned_data['paid_with_my_card']:
            Transaction.objects.create(cost=e.cost, positive=True, expense=e, user=e.added_by)
        ticket_added = True

    return render(request, 'bank/add_ticket.html', locals())

@login_required
def history_of_my_transactions(request):
    listOfTransactions = request.user.get_transactions()
    return render(request, 'bank/history_transaction.html', locals())