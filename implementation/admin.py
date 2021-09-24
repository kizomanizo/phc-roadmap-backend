from django.contrib import admin

from .models import (
    Goal, Initiative, Activity, Approach, InitiativeDetail, DetailType, Output,
    OutputType, InputType, Input
)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['name', 'goal_details', 'goal_after_investment']
    search_fields = ['name']
    list_per_page = 50


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ['name', 'goal', 'order', 'initiative_short_description']
    search_fields = ['name']
    list_per_page = 50


@admin.register(DetailType)
class DetailTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_per_page = 50


@admin.register(InitiativeDetail)
class InitiativeDetailAdmin(admin.ModelAdmin):
    # list_display = ['get_initiative', 'initiative_detail', 'get_detail_type']
    # search_fields = ['initiative__text', 'detail_type__name', 'text']
    list_per_page = 50

    """
    @admin.display(description='Initiative Name')
    def get_initiative(self, obj):
        return obj.initiative.name

    @admin.display(description='Detail Type')
    def get_detail_type(self, obj):
        return obj.detail_type.name
"""


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    # list_display = ['get_initiative', 'get_output_type', 'output_text', 'order']
    # search_fields = ['initiative__initiative', 'output_type__output_type', 'output_text']
    list_per_page = 50

    """
    @admin.display(description='Initiative Name')
    def get_initiative(self, obj):
        return obj.initiative.name

    @admin.display(description='Output Type')
    def get_output_type(self, obj):
        return obj.output_type.name
    """

@admin.register(OutputType)
class OuputTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_initiative',]
    search_fields = ['name', 'initiative__name']

    @admin.display(description='Initiative Name')
    def get_initiative(self, obj):
        return obj.initiative.name


@admin.register(Approach)
class ApproachAdmin(admin.ModelAdmin):
    list_display = ['name', 'notes', 'get_activity']
    search = ['name', 'notes', 'activity__name']

    """
    @admin.display(description='Input Sub Type')
    def get_input_sub_type(self, obj):
        return obj.input_sub_type.input_sub_type
    """
    @admin.display(description='Activity')
    def get_activity(self, obj):
        return obj.activity.name


@admin.register(InputType)
class InputTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity']
    search_fields = ['id', 'name', 'quantity']


@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'get_input_type',
        'units',
        'units_short',
        'input_short',
        'cost_usd'
    ]

    search_fields = [
        'id',
        'input_sub_type',
        'input_type__input_type',
        'units',
        'units_short',
        'cost_usd'
    ]

    @admin.display(description='Input Type')
    def get_input_type(self, obj):
        return obj.input_type.name
