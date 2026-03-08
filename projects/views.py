from django.shortcuts import render, get_object_or_404, redirect
from home.models import SiteSetting
from .models import *
# Create your views here.

def ongoing_projects(request):


    site_setting = SiteSetting.objects.order_by('-id').first()
    projects = OngoingProject.objects.select_related('category').all()

    
    context = {
        'site_setting': site_setting,
        "projects": projects
    }

    return render(request, "projects/on-going.html",context)