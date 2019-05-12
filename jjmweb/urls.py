"""jjmweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('slurm/', include('slurm.urls')),
    path('', views.index, name="toc"),
    path('versions/', views.software_versions, name="versions"),
    path('how_to_venv/', views.how_to_venv, name="how_to_venv"),
    path('how_to_slurm/', views.how_to_batch, name="how_to_slurm"),
    path('how_to_freesurfer/', views.how_to_freesurfer, name="how_to_freesurfer"),
    path('how_to_container/', views.how_to_container, name="how_to_container"),
    path('how_to_fmriprep/', views.how_to_fmriprep, name="how_to_fmriprep"),
    path('docsite/', views.docsite, name="docsite"),
    path('containers/', views.containers, name="containers"),
    path('pygest/', include('pygest.urls')),
    path('admin/', admin.site.urls),
]
