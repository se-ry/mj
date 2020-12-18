from django.shortcuts import render
from .models import Test

# Create your views here.
def home(request):
    return render(request, 'home.html', {'db':[{"log":"aa"}]})

def cron():
    Test.objects.create(log='hi!')
