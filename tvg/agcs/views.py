from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import Companies, Years

from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        return render(request, "index.html")
    else:
        return redirect("login")

def form(request):
    list_obj = []
    # for company in Companies.objects.filter(name__contains="all"):
    #     list_obj.append(company)

    for company in Companies.objects.all():
        list_obj.append(company)

    context = {"context": list_obj}
    return render(request, "companies_list.html", context)

def logout_view(request):
    logout(request)


class CompaniesListView(ListView):
    model = Companies

class CompaniesDetailView(DetailView):
    model = Companies
