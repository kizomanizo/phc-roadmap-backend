from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import (
    Goal, Initiative, Activity, InitiativeDetail, DetailType, Output,
    OutputType, InputType, InputSubType, Input
)

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # data['username'] = self.user.username
        # data['email'] = self.user.email
        data['id'] = self.user.id

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class InputTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputType
        fields  = '__all__'


class InputSubTypeSerializer(serializers.ModelSerializer):
    input_type = InputTypeSerializer()
    class Meta:
        model = InputSubType
        fields = '__all__'


class InputSerializer(serializers.ModelSerializer):
    input_sub_type = InputSubTypeSerializer()

    class Meta:
        model = Input
        fields = '__all__'



class ActivitySerializer(serializers.ModelSerializer):
    inputs= InputSerializer(many=True)

    class Meta:
        model = Activity
        # fields = ('id', 'order', 'activity', 'inputs')
        fields  = '__all__'


class InitiativeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitiativeDetail
        fields = '__all__'


class InitiativeSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True)
    # initiative_details = InitiativeDetailSerializer(many=True)

    class Meta:
        model = Initiative
        # fields = (
            # 'id',
            # 'order',
            # 'initiative',
            # 'initiative_details',
            # 'initiative_short_description',
            # 'activities'
        # )
        fields  = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    initiatives = InitiativeSerializer(many=True)

    class Meta:
        model = Goal
        # fields = (
            # 'id',
            # 'goal',
            # 'goal_details',
            # 'goal_after_investment',
            # 'initiatives'
        # )
        fields  = '__all__'
