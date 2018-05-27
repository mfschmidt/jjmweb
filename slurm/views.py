from django.shortcuts import render

import subprocess


def index(request):
    """ return a rendered template with current SLURM state information. """

    context = {'keys': {}}

    # Issue the command to the underlying shell, capturing stdout
    try:
        context['date'] = subprocess.run(
            ['date'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        context['date'] = "not even a date function"
    try:
        context['keys']['queue'] = subprocess.run(
            ['squeue', '--array'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        context['keys']['queue'] = ' no squeue found '
    try:
        context['keys']['load'] = subprocess.run(
            ['sinfo', '-o', '"%10P %10e %10m %O"'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        context['keys']['load'] = 'failed to determine server load'
    try:
        context['keys']['info'] = subprocess.run(
            ['sinfo'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        context['keys']['info'] = ' no sinfo found '
    try:
        context['version'] = subprocess.run(
            ['squeue', '--version'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        context['version'] = 'SLURM does not appear to be installed.'
    try:
        context['config'] = subprocess.run(
            ['grep', '^[^#;]', '/etc/slurm-llnl/slurm.conf'], stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    except FileNotFoundError:
        context['config'] = 'cannot get config file'

    return render(request, 'slurm/index.html', context)
