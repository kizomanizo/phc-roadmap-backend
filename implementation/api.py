from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    UserSerializer, GoalSerializer, InitiativeSerializer, ActivitySerializer, ApproachSerializer,
    InputSerializer, InputTypeSerializer, UserTokenObtainPairSerializer
)
from .models import (
    Goal, Initiative, Activity, Approach, InitiativeDetail, DetailType, Output,
    OutputType, InputType, Input
)


class UserTokenObtainPairView(TokenObtainPairView):
    """
    List the user token and all the data associated with the user.
    """
    serializer_class = UserTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    List all the Users.
    """
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated,]


class GoalViewSet(viewsets.ModelViewSet):
    """
    List all the Goals.
    """
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated,]


class InitiativeViewSet(viewsets.ModelViewSet):
    """
    List all the Initiatives.
    """
    serializer_class = InitiativeSerializer
    queryset = Initiative.objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated,]


class ActivityViewSet(viewsets.ModelViewSet):
    """
    List all the Activities.
    """
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated,]


class InputViewSet(viewsets.ModelViewSet):
    """
    List all the Inputs.
    """
    serializer_class = InputSerializer
    queryset = Input.objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated,]


class ApproachViewSet(viewsets.ModelViewSet):
    """
    List all the Approaches.
    """
    serializer_class = ApproachSerializer
    queryset = InputType.objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated,]


class InputTypeViewSet(viewsets.ModelViewSet):
    """
    List all the Input Types.
    """
    serializer_class = InputTypeSerializer
    queryset = InputType.objects.all()
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated,]
