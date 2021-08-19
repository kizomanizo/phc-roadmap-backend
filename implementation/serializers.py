from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import (
    Activity, DetailType, Goal, Initiative, InitiativeDetail, Input, InputSubType,
    InputType, Output, OutputType
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)


class InputSubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputSubType
        fields = ('input_sub_type', 'cost_usd')


class InputTypeSerializer(serializers.ModelSerializer):
    input_sub_info = InputSubTypeSerializer(many=True, read_only=True)

    class Meta:
        model = InputType
        fields = ('input_type', 'input_sub_info')


class InputSerializer(serializers.ModelSerializer):
    input_sub_type = InputSubTypeSerializer()

    class Meta:
        model = Input
        fields = ('input_name', 'quantity', 'input_sub_type')


class ActivitySerializer(serializers.ModelSerializer):
    activity_input = InputSerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        fields = ('id', 'activity', 'activity_input')


class InitiativeSerializer(serializers.ModelSerializer):
    activity_initiative = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Initiative
        fields = ('id', 'initiative', 'activity_initiative')


class GoalSerializer(serializers.ModelSerializer):
    initiative_info= InitiativeSerializer(many=True, read_only=True)

    class Meta:
        model = Goal
        fields = ('goal', 'initiative_info')
