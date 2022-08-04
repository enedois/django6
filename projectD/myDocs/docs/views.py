from django.shortcuts import render
from django.http import HttpResponse
from .models import methodTitle


def index(request):
    latest_docs = methodTitle.objects.order_by('publicationDate')
    context = {'latest_docs': latest_docs}
    return render(request,"index.html", context)


# Create your views here.
