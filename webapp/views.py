from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import GuestBook
from webapp.validate import entry_validate

# Create your views here.

status_choices = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
]


def index(request):
    entries = GuestBook.objects.filter(status='active')
    return render(request, 'index.html', context={'entries': entries})


def add_entry(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        email = request.POST.get('email')
        text = request.POST.get('text')
        status = request.POST.get('status')

        entry = GuestBook(
            author=author,
            email=email,
            text=text,
            status=status
        )

        errors = entry_validate(entry)
        if not errors:
            entry.save()
            return redirect('index')
        else:
            return render(request, 'add_entry.html',
                          context={'status_choices': status_choices, 'button_text': 'Add', 'errors': errors})

    return render(request, 'add_entry.html', context={'status_choices': status_choices, 'button_text': 'Add'})


def update_entry(request, pk):
    entry = get_object_or_404(GuestBook, pk=pk)
    if request.method == "POST":
        author = request.POST.get('author')
        email = request.POST.get('email')
        text = request.POST.get('text')
        status = request.POST.get('status')

        entry.author = author
        entry.email = email
        entry.text = text
        entry.status = status

        errors = entry_validate(entry)
        if not errors:
            entry.save()
            return redirect('index')
        else:
            return render(request, 'update_entry.html',
                          context={"entry": entry, "status_choices": status_choices, 'errors': errors})

    return render(request, 'update_entry.html', context={"entry": entry, "status_choices": status_choices})


def delete_entry(request, pk):
    entry = get_object_or_404(GuestBook, pk=pk)
    if request.method == "POST":
        user_email = request.POST.get('email')
        if entry.email == user_email:
            entry.delete()
            return redirect('index')
        else:
            return render(request, 'delete_entry.html', context={'entry': entry, 'error': 'Incorrect email'})
    return render(request, 'delete_entry.html', context={'entry': entry})
