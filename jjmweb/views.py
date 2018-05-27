from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import subprocess


def index(request):
    """ Return a rendered template with a hello message."""

    context = {}
    return render(request, 'index.html', context)  # HttpResponse(response)


def software_versions(request):
    """ Return an html page with current software versions. """

    context = {'keys': {}}

    # Issue the command to the underlying shell, capturing stdout
    try:
        context['keys']['OS'] = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        context['keys']['OS'] = "error running uname -a"
    try:
        context['keys']['Singularity'] = subprocess.run(['singularity', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        context['keys']['Singularity'] = "error running singularity --version"
    try:
        context['keys']['Apache 2'] = subprocess.run(['/usr/sbin/apache2', '-v'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        context['keys']['Apache 2'] = "error running apache2 -v"
    try:
        context['keys']['MySQL'] = subprocess.run(['mysql', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        context['keys']['MySQL'] = 'error running mysql --version'
    try:
        context['keys']['Python'] = subprocess.run(['python', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        context['keys']['Python'] = 'error running python --version'
    try:
        context['keys']['Python3'] = subprocess.run(['python3', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        context['keys']['Python3'] = 'error running python3 --version'
    try:
        context['keys']['SLURM'] = subprocess.run(['squeue', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        context['keys']['SLURM'] = 'error running squeue --version'
    try:
        context['keys']['Matlab'] = "not yet implemented"
    except FileNotFoundError:
        context['keys']['Matlab'] = 'error running matlab --version'

    return render(request, 'versions.html', context)

def how_to_batch(request):
    """ return a rendered template with instructions for SLURM job submission. """

    context = {}
    return render(request, 'how_to_batch.html', context)


def how_to_venv(request):
    """ return a rendered template with instructions for python virtualenvs. """

    context = {}
    return render(request, 'how_to_venv.html', context)
