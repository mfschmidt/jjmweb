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
    response += "<h2>Software versions</h2>\n"
    response += "<p><a href=\"/versions/\">Current installed software</a></p>\n"
    response += "<h2>Cluster status</h2>\n"
    response += "<p><a href=\"/slurm/\">The current SLURM queue</a></p>\n"
    response += "<h2>PyGEST</h2>\n"
    response += "<p><a href=\"/pygest/\">PyGEST coming soon</a></p>\n"

    return HttpResponse(response)


def software_versions(request):
    """ Return an html page with current software versions. """

    # Issue the command to the underlying shell, capturing stdout
    try:
        os_version = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        os_version = "error running uname -a"
    try:
        singularity_version = subprocess.run(['singularity', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        singularity_version = "error running singularity --version"
    try:
        apache2_version = subprocess.run(['/usr/sbin/apache2', '-v'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        apache2_version = "error running apache2 -v"
    try:
        mysql_version = subprocess.run(['mysql', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        mysql_version = 'error running mysql --version'
    try:
        python_version = subprocess.run(['python', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        python_version = 'error running python --version'
    try:
        python3_version = subprocess.run(['python3', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        python3_version = 'error running python3 --version'
    try:
        slurm_version = subprocess.run(['squeue', '--version'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_version = 'error running squeue --version'

    # Formulate the html to return (This should be made a template, eventually)
    response = "<h1>Software versions running here</h1>\n"

    response += "<h2>OS</h2>\n"
    response += "<div style=\"background-color: black; color: white; \"><p>\n<pre>{}</pre></p></div>\n".format(
        os_version
    )
    response += "<h2>Singularity</h2>\n"
    response += "<div style=\"background-color: black; color: white; \"><p>\n<pre>{}</pre></p></div>\n".format(
        singularity_version
    )
    response += "<h2>SLURM</h2>\n"
    response += "<div style=\"background-color: black; color: white; \"><p>\n<pre>{}</pre></p></div>\n".format(
        slurm_version
    )
    response += "<h2>apache2</h2>\n"
    response += "<div style=\"background-color: black; color: white; \"><p>\n<pre>{}</pre></p></div>\n".format(
        apache2_version
    )
    response += "<h2>MySQL</h2>\n"
    response += "<div style=\"background-color: black; color: white; \"><p>\n<pre>{}</pre></p></div>\n".format(
        mysql_version
    )
    response += "<h2>python *</h2>\n"
    response += "<div style=\"background-color: black; color: white; \"><p>\n<pre>{}</pre></p></div>\n".format(
        python_version
    )
    response += "<h2>python3 *</h2>\n"
    response += "<div style=\"background-color: black; color: white; \"><p>\n<pre>{}</pre></p></div>\n".format(
        python3_version
    )
    # response += "<p>\nDate: {}</p>\n".format(slurm_date)
    response += "<p>* It is strongly recommended, to avoid conflicts with other users, to create your own"
    response += " <a href=\"/how_to_venv/\">virtual environments</a> for python use.</p>\n"

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
