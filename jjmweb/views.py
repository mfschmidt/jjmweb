from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import subprocess


def index(request):
    """
    :param request:
    :return: html table of contents

    """

    # Formulate the html to return (This should be made a template, eventually)
    response = "<h2>Instructions</h2>\n"
    response += "<p><a href=\"/how_to_batch/\">How to create a SLURM batch file</a></p>\n"
    response += "<p><a href=\"/how_to_venv/\">How to create your user-specific python environment</a></p>\n"
    response += "<h2>Cluster status</h2>\n"
    response += "<p><a href=\"/slurm/\">The current SLURM queue</a></p>\n"

    return HttpResponse(response)


def how_to_batch(request):
    """

    :param request:
    :return:
    """

    doc_url = "https://slurm.schedmd.com/sbatch.html"
    harvard_url = "https://www.rc.fas.harvard.edu/resources/running-jobs/#Submitting_batch_jobs_using_the_sbatch_command"
    rutgers_url = "http://ecs.rutgers.edu/slurm_commands.html"
    response = "<h2>SLURM batch files</h2>\n"
    response += "<p>Mike has not written any how-to docs yet.</p>\n"
    response += "<p>Please see resources from <a href=\"{h}\">Harvard</a> or <a href=\"{r}\">Rutgers</a> for now.</p>"
    response += "<p>Or you may want to read the <a href=\"{d}\">documentation</a>.</p>"

    return HttpResponse(response.format(h=harvard_url, r=rutgers_url, d=doc_url))


def how_to_venv(request):
    """

    :param request:
    :return:
    """

    doc_url = "https://docs.python.org/3/library/venv.html"
    motw_url = "https://pymotw.com/3/venv/"
    response = "<h2>Virtual Environments</h2>\n"
    response += "<p>Mike has not written any how-to docs yet.</p>\n"
    response += "<p>Please see resources from <a href=\"{motw}\">Module of the week</a> for now. "
    response += "or read the <a href=\"{d}\">documentation</a>.</p>"

    return HttpResponse(response.format(motw=motw_url, d=doc_url))
