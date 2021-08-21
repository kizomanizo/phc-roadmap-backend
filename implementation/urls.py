from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from .api import (
     UserViewSet, GoalViewSet, InitiativeViewSet,ActivityViewSet,
     InputViewSet, InputSubTypeViewSet, InputTypeViewSet, UserTokenObtainPairView

)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('data', GoalViewSet, basename='data')
router.register('initiative', InitiativeViewSet, basename='initiative')
router.register('activity', ActivityViewSet, basename='activity')
router.register('input', InputViewSet, basename='input')
router.register('input-sub-type', InputSubTypeViewSet, basename='input-sub-type')
router.register('input-type', InputTypeViewSet, basename='input-type')

urlpatterns = [
    path('users/login/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
]

urlpatterns += router.urls
