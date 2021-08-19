from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import (
    Activity, DetailType, Goal, Initiative, InitiativeDetail, Input, InputSubType,
    InputType, Output, OutputType
)
from .serializers import (
    UserSerializer, GoalSerializer, InitiativeSerializer, ActivitySerializer,
    InputSerializer, InputSubTypeSerializer, InputTypeSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    List all the Users.
    """
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    http_method_names = ['get']


class GoalViewSet(viewsets.ModelViewSet):
    """
    List all the Goals.
    """
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()
    http_method_names = ['get']


class InitiativeViewSet(viewsets.ModelViewSet):
    """
    List all the Initiatives.
    """
    serializer_class = InitiativeSerializer
    queryset = Initiative.objects.all()
    http_method_names = ['get']


class ActivityViewSet(viewsets.ModelViewSet):
    """
    List all the Activities.
    """
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    http_method_names = ['get']


class InputViewSet(viewsets.ModelViewSet):
    """
    List all the Inputs.
    """
    serializer_class = InputSerializer
    queryset = Input.objects.all()
    http_method_names = ['get']


class InputSubTypeViewSet(viewsets.ModelViewSet):
    """
    List all the Input Sub Types.
    """
    serializer_class = InputSubTypeSerializer
    queryset = InputSubType.objects.all()
    http_method_names = ['get']


class InputTypeViewSet(viewsets.ModelViewSet):
    """
    List all the Input Types.
    """
    serializer_class = InputTypeSerializer
    queryset = InputType.objects.all()
    http_method_names = ['get']