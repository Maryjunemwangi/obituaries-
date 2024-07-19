from django.shortcuts import render, redirect
from .models import Obituary
from django.utils.text import slugify
from django.utils import timezone

def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        date_of_death = request.POST.get('date_of_death')
        content = request.POST.get('content')
        author = request.POST.get('author')
        submission_date = timezone.now()
        slug = slugify(name + "-" + date_of_death)

        Obituary.objects.create(
            name=name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            content=content,
            author=author,
            submission_date=submission_date,
            slug=slug
        )
        return redirect('view_obituaries')
    return render(request, 'obituary_form.html')


def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})
