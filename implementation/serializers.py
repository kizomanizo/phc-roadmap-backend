from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import (
    Activity, DetailType, Goal, Initiative, InitiativeDetail, Input, InputSubType,
    InputType, Output, OutputType
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


class InputSubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputSubType
        exclude = ('input_type', )


class InputTypeSerializer(serializers.ModelSerializer):
    input_sub_types = InputSubTypeSerializer(many=True)

    class Meta:
        model = InputType
        fields = ('id', 'input_type', 'input_sub_types')


class InputSerializer(serializers.ModelSerializer):
    input_sub_type = InputSubTypeSerializer()

    class Meta:
        model = Input
        exclude = ('activity', )


class ActivitySerializer(serializers.ModelSerializer):
    inputs = InputSerializer(many=True)

    class Meta:
        model = Activity
        fields = ('id', 'order', 'activity', 'inputs')


class InitiativeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitiativeDetail
        fields = '__all__'


class InitiativeSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True)
    initiative_details = InitiativeDetailSerializer(many=True)

    class Meta:
        model = Initiative
        fields = (
            'id',
            'order',
            'initiative',
            'initiative_details',
            'initiative_short_description',
            'activities'
        )


class GoalSerializer(serializers.ModelSerializer):
    initiatives = InitiativeSerializer(many=True)

    class Meta:
        model = Goal
        fields = (
            'id',
            'goal',
            'goal_details',
            'goal_after_investment',
            'initiatives'
        )
