from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse

from app.models import JobPost, Location

job_title = [
    'First Jobs',
    'Second Jobs',
    "Third Jobs"
]

job_description = [
    "First Job description",
    "Second Job description",
    "Third Job  description"
]


def hello(request):
    lenguajes = ['Ruby', 'css', 'javascript', 'Python', 'Flutter']
    context = {
        'nombre': 'Rodrigo',
        'apellido': 'Pasten',
        'lenguajes': lenguajes,
        'direccion': 'El Cobre 3838'
    }
    return render(request, 'hello.html', context)


def job_list(request):
    #list_of_jobs = "<ul>"
    #for j in job_title:
      #  job_id = job_title.index(j)
        #detail_url = reverse('job_detail', args=(job_id,))
        #list_of_jobs += f"<li><a href = '{detail_url}'>{j} </li>"
    #list_of_jobs += "</ul>"

    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, "index.html", context)


def job_detail(request, slug):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))

        job = JobPost.objects.get(slug=slug)

        context = {"job": job}
        return render(request, 'job_detail.html', context)
    except:
        return HttpResponseNotFound('No encontrado')

