from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, timedelta
from supper.models import Day, Participation
from users.models import CustomUser

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('day', type=int)
        parser.add_argument('month', type=int)
        parser.add_argument('year', type=int)

    def handle(self, *args, **options):
        firstDate = datetime(options['year'], options['month'], options['day'])
        internalUsers = CustomUser.objects.filter(internal=True)
        days = Day.objects.filter(date__gt=firstDate)
        for user in internalUsers:
            for day in days:
                if not Participation.objects.filter(user=user, day=day).exists():
                    Participation.objects.create(user=user, day=day)
