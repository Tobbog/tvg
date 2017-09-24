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
    #     return HttpResponse("is authenticated")
    # else:
    #     return HttpResponse("not authenticated")

def logout_view(request):
    logout(request)


class CompaniesListView(ListView):
    model = Companies

class CompaniesDetailView(DetailView):
    model = Companies
