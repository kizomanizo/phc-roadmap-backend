from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Sum, F, Prefetch
from django.db import connection

"""
from implementation.models import (
    Activity, DetailType, Goal, Initiative, InitiativeDetail, Input, InputSubType,
    InputType, Output, OutputType
)


def index(request):
    """Return the home page for the reports"""
    return render(request, 'implementation/index.html')


def detailed_report(request):
    """Return the home page for the reports"""
    # initiatives_with_activies_n_goals= list(
    #     Initiative.objects.select_related('goal').\
    #         values(
    #             'id', 'initiative', 'order', 'goal__goal', 'goal__goal_details',
    #         )
    # )
    # all_initiatives = list(Initiative.objects.prefetch_related('actvity_set')
        # prefetch_related('activity_set')
        # values('id', 'initiative', 'goal__goal', 'goal__goal_details')   
    # )

    # activities_with_inputs = list(
    #     Activity.objects.prefetch_related('input_set').\
    #     filter()
    # )
    # all_inputs = list(
    #     Input.objects.select_related('input_sub_type__input_type').\
    #     select_related('activity').all()
    # )

    with connection.cursor() as cursor:
        cursor.execute(
        """
        select i.id, i.initiative, gl.goal, gl.goal_details, act.activity, inp.input_name,
        inp.quantity, inp_sub.input_sub_type, inp_sub.cost_usd, inp_type.input_type,
        (inp_sub.cost_usd * inp.quantity) as calculated_cost

        from "tblInitiatives" i, "tblGoals" gl, "tblActivities" act, "tblInputs" inp,
        "tblListInputSubTypes" inp_sub, "tblListInputTypes" inp_type

        where 
        i.goal_id=gl.id and act.initiative_id=i.id
        and act.id=inp.activity_id and inp.input_sub_type_id=inp_sub.id
        and inp_sub.input_type_id=inp_type.id;

        """
        )
        results = cursor.fetchall()
    
    
    return render(request, 'implementation/detailed_report_view.html', {'results': results})


def summary_report(request):
    """Return the home page for the reports"""
    return render(request, 'implementation/summary_report_view.html')


def summary_investment_report(request):
    """Return the home page for the reports"""
    return render(request, 'implementation/index.html')


def export_detailed_pdf(request):
    """The view for generating the pdf file for the detailed report."""
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
        'implementation/detailed_report.html',
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


def export_summary_pdf(request):
    """The view for generating the pdf file for the summary report."""
    today = datetime.now()
    #  sum = Activities.object.filter().aggregrate(Sum('quantity'))
    context = {
        'expenses': [],
        'total': 0
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; attachment; filename=Summary Report{today}.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    html_string = render_to_string(
        'implementation/summary_report.html',
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


def export_summary_investment_pdf(request):
    """The view for generating the pdf file for the report."""
    today = datetime.now()
    #  sum = Activities.object.filter().aggregrate(Sum('quantity'))
    context = {
        'expenses': [],
        'total': 0
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; attachment; filename=Summary Report{today}.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    html_string = render_to_string(
        'implementation/investment_summary_report.html',
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
"""
