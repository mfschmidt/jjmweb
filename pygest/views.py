import os

from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps

from . import helpers

def index(request):
    error = None
    try:
        base_path = apps.get_app_config("pygest").pygest_data
        deriv_path = os.path.join(base_path, "derivatives")
        shuffle_path = os.path.join(base_path, "shuffles")
        deriv_results = helpers.get_results(deriv_path)
        shuffle_results = helpers.get_results(shuffle_path)
    except KeyError:
        error = "pygest_data is not accessible as an app trait."
        results = []
    response = "<html>\n<head>\n"
    response += "  <title>PyGEST</title>\n"
    response += "</head>\n<body>\n"
    response += "<p>PyGEST is not yet implemented. The following page is either placeholder or testing data.</p>\n"
    if error is not None:
        response += "<p class=\"error\">{}</p>".format(error)
    else:
        response += "<h2>Results</h2>\n"
        response += "<table>\n"
        response += "  <tr><th>{sub}</th><th>{hem}</th><th>{ctx}</th><th>{tgt}</th><th>{alg}</th><th>{file}</th><th>{note}</th></tr>\n".format(
            sub="sub",
            hem="hem",
            ctx="ctx",
            tgt="tgt",
            alg="alg",
            file="file",
            note="note"
        )
        for result in deriv_results:
            response += "  <tr><td>{sub}</td><td>{hem}</td><td>{ctx}</td><td>{tgt}</td><td>{alg}</td><td>{file}</td><td>{note}</td></tr>\n".format(
                sub=result.get("sub", " "),
                hem=result.get("hem", " "),
                ctx=result.get("ctx", " "),
                tgt=result.get("tgt", " "),
                alg=result.get("alg", " "),
                file=result.get("file", " "),
                note="-",  # result.get("note", "NO NOTE"),
            )
        response += "</table>\n"
    response += "<p>Try later for status and results information.</p>\n"
    response += "</body>\n</html>\n"
    return HttpResponse(response)
