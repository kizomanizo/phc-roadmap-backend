from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detailed-report-pdf', views.export_detailed_pdf,
         name='export_detailed_pdf'),
    path('summary-report-pdf', views.export_summary_pdf,
         name='export_summary_pdf'),
    path('summary-investment-report-pdf', views.export_summary_investment_pdf,
         name='export_summary_investment_pdf'),
]
