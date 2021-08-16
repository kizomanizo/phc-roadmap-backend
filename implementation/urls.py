from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detailed-report', views.detailed_report,
         name='detailed_report'),
    path('summary-report', views.summary_report,
         name='summary_report'),
    path('summary-investment-report', views.summary_investment_report,
         name='summary_investment_report'),

    # Report Generation URLs
    path('detailed-report-pdf', views.export_detailed_pdf,
         name='export_detailed_pdf'),
    path('summary-report-pdf', views.export_summary_pdf,
         name='export_summary_pdf'),
    path('summary-investment-report-pdf', views.export_summary_investment_pdf,
         name='export_summary_investment_pdf'),
]
