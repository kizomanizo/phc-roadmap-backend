from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Sum


def index(request):
    """Return the home page for the reports"""
    return render(request, 'implementation/index.html')


def export_pdf(request):
    """The view for generating the pdf file for the report."""
    today = datetime.now()
    #  sum = Activities.object.filter().aggregrate(Sum('quantity'))
    context = {
        'expenses': [],
        'total': 0
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; attachment; filename=Activities_{today}.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    html_string = render_to_string(
        'implementation/pdf_report.html',
        context
    )
    html = HTML(string=html_string)

    result = html.write_pdf(stylesheets=['staticfiles/css/styles.css'])

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        output = open(output.name, 'rb')
        response.write(output.read())

    return response
