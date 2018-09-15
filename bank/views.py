from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm, AddMoneyForm
from .models import Expense, Transaction
from datetime import datetime, timedelta, date

# Create your views here.
@login_required
def add_ticket(request):
    page_name = 'Ajouter un ticket'
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
            Transaction.objects.create(cost=e.cost, positive=True,
                expense=e, user=e.added_by)
        ticket_added = True

    return render(request, 'bank/form.html', locals())

@login_required
def add_money(request):
    page_name = "Ajouter de l'argent"
    form = AddMoneyForm(request.POST or None)
    if form.is_valid() and request.user.treasurer:
        e = form.save(commit=False)
        e.positive = True
        e.added_by = request.user
        e.kot = request.user.kot
        e.save()
        Transaction.objects.create(cost=e.cost, positive=True,
            expense=e, user=form.cleaned_data['user'])
        ticket_added = True
    return render(request, 'bank/form.html', locals())

@login_required
def history_of_my_transactions(request):
    listOfTransactions = request.user.get_transactions
    return render(request, 'bank/history_transaction.html', locals())

@login_required
def history_transactions_commu(request):
    listOfTransactions = Expense.objects.filter(kot=request.user.kot).order_by('-date')
    return render(request, 'bank/history_transaction.html', locals())

@login_required
def charts(request):
    firstday = datetime.now() - timedelta(30)
    label = []
    value1 = []
    value2 = []
    for i in range(1,31):
        currentDate = firstday + timedelta(i)
        label.append("{: %d/%m/%y}".format(currentDate))
        value1.append(int(balance_on_a_date(currentDate, request.user)))
        value2.append(int(balance_on_a_date_expense(currentDate, request.user.kot)))
    data = {
        'label': label,
        'value1': value1,
        'value2': value2,
    }
    return render(request, 'bank/charts.html', locals())

def balance_on_a_date_expense(date, kot):
    listOfTransactions = Expense.objects.filter(date__lte=date, kot=kot)
    return sum_transactions(listOfTransactions)

def balance_on_a_date(date, user):
    listOfTransactions = Transaction.objects.filter(expense__date__lte=date, user=user)
    return sum_transactions(listOfTransactions)

def sum_transactions(listOfTransactions):
    balance = 0
    for t in listOfTransactions:
        if t.positive:
            balance += t.cost
        else:
            balance -= t.cost
    return balance
