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

        data['username'] = self.user.username
        data['email'] = self.user.email

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = ['id', 'username', 'email', 'first_name', 'last_name']
        fields = '__all__'


class InputSubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputSubType
        # fields = ('id','input_sub_type', 'cost_usd')
        fields = '__all__'


class InputTypeSerializer(serializers.ModelSerializer):
    input_sub_info = InputSubTypeSerializer(many=True, read_only=True)

    class Meta:
        model = InputType
        # fields = ('id', 'input_type', 'input_sub_info')
        fields = '__all__'


class InputSerializer(serializers.ModelSerializer):
    input_sub_type = InputSubTypeSerializer()

    class Meta:
        model = Input
        # fields = ('id', 'input_name', 'quantity', 'input_sub_type')
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    activity_input = InputSerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        # fields = ('id', 'activity', 'activity_input')
        fields =  '__all__'


class InitiativeSerializer(serializers.ModelSerializer):
    activity_initiative = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = Initiative
        # fields = ('id', 'initiative', 'activity_initiative')
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    initiative_info= InitiativeSerializer(many=True, read_only=True)

    class Meta:
        model = Goal
        # fields = ('id', 'goal', 'initiative_info')
        fields = '__all__'
