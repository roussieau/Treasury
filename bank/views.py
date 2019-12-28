from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm, AddMoneyForm
from .models import Expense, Transaction
from datetime import datetime, timedelta, date
from users.models import CustomUser
from django.core.paginator import Paginator

# Create your views here.
@login_required
def add_ticket(request):
    page_name = 'Ajouter un ticket'
    bank_page = 'active'
    if request.POST:
        form = ExpenseForm(request.user, request.POST)
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
    else:
        form = ExpenseForm(user=request.user)

    return render(request, 'bank/form.html', locals())

@login_required
def add_money(request):
    page_name = "Ajouter de l'argent"
    form = AddMoneyForm(user=request.user)

    if request.POST:
        form = AddMoneyForm(request.user, request.POST)
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
def expenses_history(request):
    expenses = Expense.objects.filter(kot=request.user.kot).order_by('-date')
    return render(request, 'bank/history_expenses.html', locals())

@login_required
def expense_delete(request, id):
    expense = Expense.objects.get(id=id)
    expense.remove()
    return redirect('bank:expenses_history')


@login_required
def status(request):
    listOfUsers = CustomUser.objects.filter(kot=request.user.kot).order_by('first_name', 'last_name')
    status = compute_status(listOfUsers)
    return render(request, 'bank/status.html', {'status': status})

@login_required
def history_of_my_transactions(request):
    listOfTransactions = request.user.get_transactions()
    paginator = Paginator(listOfTransactions, 20)
    dept = compute_debt(listOfTransactions)

    page = request.GET.get('page')
    transactions = paginator.get_page(page)
    return render(request, 'bank/history_transaction.html', locals())

@login_required
def history_transactions_commu(request):
    listOfTransactions = Expense.objects.filter(kot=request.user.kot).order_by('-date')
    return render(request, 'bank/history_transaction.html', locals())

@login_required
def charts(request):
    listOfUsers = CustomUser.objects.filter(kot=request.user.kot).order_by('first_name', 'last_name')
    names = []
    status = []
    colors = []
    for u in listOfUsers:
        transactions = Transaction.objects.filter(user=u)
        user_balance = 0
        for transaction in transactions:
            if transaction.positive:
                user_balance += transaction.cost
            else:
                user_balance -= transaction.cost
        names.append(u.get_full_name())
        status.append(float(user_balance))
        colors.append('#33cc33') if user_balance > 0 else colors.append('#ff4d4d')
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


def compute_status(listOfUsers):
    status = []
    for user in listOfUsers:
        transactions = Transaction.objects.filter(user=user)
        user_balance = 0
        for transaction in transactions:
            if transaction.positive:
                user_balance += transaction.cost
            else:
                user_balance -= transaction.cost
        status.append({'name': user.get_full_name(), 'balance': user_balance})
    return status


def compute_debt(listOfTransactions):
    count = 0
    for t in listOfTransactions:
        if not t.positive:
            count += t.cost
    return count
