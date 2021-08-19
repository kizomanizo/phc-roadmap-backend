# from django.urls import path
from rest_framework.routers import DefaultRouter
# from . import views
from .api import (
     UserViewSet, GoalViewSet, InitiativeViewSet,ActivityViewSet,
     InputViewSet, InputSubTypeViewSet, InputTypeViewSet

)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('data', GoalViewSet, basename='goals')
router.register('initiative', InitiativeViewSet, basename='initiative')
router.register('activity', ActivityViewSet, basename='activity')
router.register('input', InputViewSet, basename='input')
router.register('input-sub-type', InputSubTypeViewSet, basename='input-sub-type')
router.register('input-type', InputTypeViewSet, basename='input-type')

"""
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
"""

urlpatterns = router.urls