from django.http import HttpResponse

import subprocess


def index(request):
    """
    :param request:
    :return: html representing the output of the slurm command

    """

    # Issue the command to the underlying shell, capturing stdout
    try:
        slurm_date = subprocess.run(['date'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_date = "not even a date function"
    try:
        slurm_queue = subprocess.run(['squeue'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_queue = ' no squeue found '
    try:
        slurm_info = subprocess.run(['sinfo'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_info = ' no sinfo found '
    try:
        slurm_version = subprocess.run(['squeue --version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_version = 'SLURM does not appear to be installed.'

    # Formulate the html to return (This should be made a template, eventually)
    response = "<h2>squeue</h2>\n"
    response += "<div style=\"background-color: black; color: white; \"><p>\n{}</p></div>\n".format(slurm_queue)
    response += "<h2>sinfo</h2>\n"
    response += "<div style=\"background-color: black; color: white; \"><p>\n{}</p></div>\n".format(slurm_info)
    response += "<p>\nVersion: {}</p>\n".format(slurm_version)
    response += "<p>\nDate: {}</p>\n".format(slurm_date)

    return HttpResponse(response)
