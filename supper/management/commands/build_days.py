from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta
from supper.models import Day

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('day', type=int)
        parser.add_argument('month', type=int)
        parser.add_argument('year', type=int)
        parser.add_argument('nbrOfWeek', type=int)
        parser.add_argument('start', type=int)

    def handle(self, *args, **options):
        firstDate = datetime(options['year'], options['month'], options['day'])
        
        for i in range(0, options['nbrOfWeek']):
            for j in range(0, 4):
                Day.objects.create(date=(firstDate + timedelta(days=i*7+j)), 
                        week=options['start']+i, visible=True)
