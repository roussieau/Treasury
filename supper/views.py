from django.shortcuts import render
from .models import Day

# Create your views here.
def planning(request):
    daysObject = Day.objects.all()
    days = []
    for d in daysObject:
        day = d
        presence = d.presence(request.user)
        days.append({'day':day,
                     'presence':presence})
    return render(request, 'supper/planning.html', locals())
