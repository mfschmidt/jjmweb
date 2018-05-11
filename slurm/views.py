from django.http import HttpResponse

import subprocess


def index(request):
    """
    :param request:
    :return: html representing the output of the slurm command

    """

    # Issue the command to the underlying shell, capturing stdout
    try:
        slurm_date = subprocess.run(
            ['date'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_date = "not even a date function"
    try:
        slurm_queue = subprocess.run(
            ['squeue'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_queue = ' no squeue found '
    try:
        slurm_info = subprocess.run(
            ['sinfo'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_info = ' no sinfo found '
    try:
        slurm_version = subprocess.run(
            ['squeue', '--version'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_version = 'SLURM does not appear to be installed.'
    try:
        slurm_config = subprocess.run(
            ['grep', '^[^#;]', '/etc/slurm-llnl/slurm.conf'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        slurm_config = 'cannot get config file'

    # Formulate the html to return (This should be made a template, eventually)
    response = "<h2>Cluster information</h2>\n"
    response += "<div style=\"background-color: white; color: black; \"><p>\n<pre>{}</pre></p></div>\n".format(
        "sinfo"
    )
    response += "<div style=\"background-color: black; color: white; \"><p>\n<pre>{}</pre></p></div>\n".format(
        slurm_info
    )
    response += "<h2>Current queue</h2>\n"
    response += "<div style=\"background-color: white; color: black; \"><p>\n<pre>{}</pre></p></div>\n".format(
        "squeue"
    )
    response += "<div style=\"background-color: black; color: white; \"><p>\n<pre>{}</pre></p></div>\n".format(
        slurm_queue
    )
    response += "<h2>Configuration</h2>\n"
    response += "<div style=\"background-color: white; color: black; \"><p>\n<pre>{}</pre></p></div>\n".format(
        "grep \"^[^#;]\" /etc/slurm-llnl/slurm.conf"
    )
    response += "<div style=\"background-color: black; color: white; \"><p>\n<pre>{}</pre></p></div>\n".format(
        slurm_config
    )
    response += "<p>\nVersion: {}</p>\n".format(slurm_version)
    response += "<p>\nDate: {}</p>\n".format(slurm_date)

    return HttpResponse(response)
