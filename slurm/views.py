from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import subprocess


def index(request):
    """
    :param request:
    :return: html representing the output of the slurm command

    """

    # Issue the command to the underlying shell, capturing stdout
    try:
        slurm_queue = subprocess.run(['squeue'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        slurm_version = subprocess.run(['squeue --version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_queue = ' '
        slurm_version = 'SLURM does not appear to be installed.'

    # Formulate the html to return (This should be made a template, eventually)
    response = "<h2>squeue</h2>\n"
    response += "<div style=\"background-color: black; color: white; \"><p>\n{}</p></div>\n".format(slurm_queue)
    response += "<p>\nVersion: {}</p>\n".format(slurm_version)

    return HttpResponse(response)
