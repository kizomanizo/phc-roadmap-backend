from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from .api import (
    UserViewSet, GoalViewSet, InitiativeViewSet,ActivityViewSet, InputViewSet,
    InputSubTypeViewSet, InputTypeViewSet, UserTokenObtainPairView
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('data', GoalViewSet, basename='data')
router.register('initiatives', InitiativeViewSet, basename='initiatives')
router.register('goals', GoalViewSet, basename='goals')
router.register('activities', ActivityViewSet, basename='activities')
router.register('inputs', InputViewSet, basename='inputs')
router.register('input-subtypes', InputSubTypeViewSet, basename='input-subtypes')
router.register('input-types', InputTypeViewSet, basename='input-types')

urlpatterns = [
    path('users/login/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
]

urlpatterns += router.urls
