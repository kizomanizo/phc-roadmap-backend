from django.contrib import admin

from .models import (
    Goal, Initiative, Activity, InitiativeDetail, DetailType, Output,
    OutputType, InputType, InputSubType, Input
)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['name', 'goal_details', 'goal_after_investment']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_goal', 'order', 'initiative_short_description']
    search_fields = ['name', 'goal__name']
    list_per_page = 20

    @admin.display(description='Goal')
    def get_goal(self, obj):
        return obj.goal.name


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_initiative',]
    search_fields = ['name', 'initiative__name']

    @admin.display(description='Initiative Name')
    def get_initiative(self, obj):
        return obj.initiative.name


@admin.register(InputType)
class InputTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(InputSubType)
class InputSubTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'get_input_type',
        'units',
        'units_short',
        'cost_usd'
    ]
    search_fields = ['id', 'name', 'input_type__name', 'units', 'cost_usd']

    @admin.display(description='Input Type')
    def get_input_type(self, obj):
        return obj.input_type.name


@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'get_input_sub_type',
        'quantity',
        'notes',
    ]

    search_fields = [
        'id',
        'name',
        'input_sub_type__name',
        'quantity',
        'notes',
    ]

    @admin.display(description='Input Sub Type')
    def get_input_sub_type(self, obj):
        return obj.input_sub_type.name


@admin.register(DetailType)
class DetailTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    list_per_page = 20


@admin.register(InitiativeDetail)
class InitiativeDetailAdmin(admin.ModelAdmin):
    list_display = ['get_initiative', 'get_detail_type', 'text']
    search_fields = ['initiative__name', 'detail_type__name', 'text']
    list_per_page = 20

    @admin.display(description='Initiative Name')
    def get_initiative(self, obj):
        return obj.initiative.name

    @admin.display(description='Detail Type')
    def get_detail_type(self, obj):
        return obj.detail_type.name


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = ['get_initiative', 'get_output_type', 'description', 'order']
    search_fields = [
        'initiative__name',
        'output_type__name',
        'description'
    ]
    list_per_page = 20

    @admin.display(description='Initiative Name')
    def get_initiative(self, obj):
        return obj.initiative.name

    @admin.display(description='Output Type')
    def get_output_type(self, obj):
        return obj.output_type.name


@admin.register(OutputType)
class OuputTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
