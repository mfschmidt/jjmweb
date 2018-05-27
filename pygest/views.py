import os

from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps

from . import helpers


def entable(items):
    response = "<table>\n"
    response += "  <tr>" + "<th>{sub}</th><th>{hem}</th><th>{ctx}</th><th>{tgt}</th><th>{alg}</th><th>{cmp}</th><th>{msk}</th><th>{adj}</th><th>{file}</th></tr>\n".format(
        sub="sub",
        hem="hem",
        ctx="ctx",
        tgt="tgt",
        alg="alg",
        cmp="cmp",
        msk="msk",
        adj="adj",
        file="file",
        note="note"
    )
    for result in items:
        response += "  <tr><td>{sub}</td><td>{hem}</td><td>{ctx}</td><td>{tgt}</td><td>{alg}</td><td>{cmp}</td><td>{msk}</td><td>{adj}</td><td>{file}</td></tr>\n".format(
            sub=result.get("sub", " "),
            hem=result.get("hem", " "),
            ctx=result.get("ctx", " "),
            tgt=result.get("tgt", " "),
            alg=result.get("alg", " "),
            cmp=result.get("cmp", " "),
            msk=result.get("msk", " "),
            adj=result.get("adj", " "),
            file=result.get("file", " "),
            note="-",  # result.get("note", "NO NOTE"),
        )
    response += "</table>\n"
    return response


def index(request):
    error = None
    try:
        base_path = apps.get_app_config("pygest").pygest_data
        deriv_path = os.path.join(base_path, "derivatives")
        deriv_results = helpers.get_results(deriv_path)
        shuffle_path = os.path.join(base_path, "shuffles")
        shuffle_results = helpers.get_results(shuffle_path)
        dist_shuffle_path = os.path.join(base_path, "distshuffles")
        dist_shuffle_results = helpers.get_results(shuffle_path)
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
        response += entable(deriv_results)
        response += "<h2>Raw Shuffles</h2>\n"
        response += entable(shuffle_results)
        response += "<h2>Distance-aware Shuffles</h2>\n"
        response += entable(dist_shuffle_results)
    response += "<p>Try later for status and results information.</p>\n"
    response += "</body>\n</html>\n"
    return HttpResponse(response)
