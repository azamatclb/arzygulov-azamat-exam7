from django.shortcuts import render

from webapp.models import GuestBook


# Create your views here.

def index(request):
    entries = GuestBook.objects.filter(status='active')
    return render(request, 'index.html', context={'entries': entries})


