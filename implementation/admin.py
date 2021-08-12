from django.contrib import admin
from .models import Goal, Initiative, InitiativeDetail, OutputType, Activity, DetailType, Input, InputType, InputSubType, Output


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['goal', 'goal_details', 'goal_after_investment']
    search_fields = ['goal']
    list_per_page = 50


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ['initiative', 'goal', 'order', 'initiative_short_description']
    search_fields = ['iniative']
    list_per_page = 50


@admin.register(DetailType)
class DetailTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'detail_type']
    search_fields = ['id']
    list_per_page = 50


@admin.register(InitiativeDetail)
class InitiativeDetailAdmin(admin.ModelAdmin):
    list_display = ['get_initiative', 'initiative_detail', 'get_detail_type']
    search_fields = ['initiative__initiative', 'detail_type__detail_type', 'initiative_detail']
    list_per_page = 50

    @admin.display(description='Initiative Name')
    def get_initiative(self, obj):
        return obj.initiative.initiative

    @admin.display(description='Detail Type')
    def get_detail_type(self, obj):
        return obj.detail_type.detail_type


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = ['get_initiative', 'get_output_type', 'output_text', 'order']
    search_fields = ['initiative__initiative', 'output_type__output_type', 'output_text']

    @admin.display(description='Initiative Name')
    def get_initiative(self, obj):
        return obj.initiative.initiative

    @admin.display(description='Output Type')
    def get_output_type(self, obj):
        return obj.output_type.output_type


@admin.register(OutputType)
class OuputTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'output_type']
    search_fields = ['id', 'output_type']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['activity', 'get_initiative']
    search_fields = ['activity', 'initiative__initiative']

    @admin.display(description='Initiative Name')
    def get_initiative(self, obj):
        return obj.initiative.initiative


@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    list_display = ['input_name', 'get_input_sub_type', 'quantity', 'get_activity']
    search = ['input_name' 'input_sub_type__input_sub_type', 'quantity', 'activity__activity']

    @admin.display(description='Input Sub Type')
    def get_input_sub_type(self, obj):
        return obj.input_sub_type.input_sub_type

    @admin.display(description='Activity')
    def get_activity(self, obj):
        return obj.activity.activity


@admin.register(InputType)
class InputTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'input_type']
    search_fields = ['id', 'input_type']


@admin.register(InputSubType)
class InputSubTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'input_sub_type',
        'get_input_type',
        'units',
        'units_short',
        'input_sub_type_short',
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
        return obj.input_type.input_type

