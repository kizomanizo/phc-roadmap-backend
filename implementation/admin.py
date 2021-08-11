from django.contrib import admin
from .models import Goal, Initiative, InitiativeDetail, OutputType, Activity, DetailType, Input, InputType, InputSubType, Output


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    pass


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    pass


@admin.register(DetailType)
class DetailTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(InitiativeDetail)
class InitiativeDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    pass


@admin.register(OutputType)
class OuputTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    pass


@admin.register(InputType)
class InputTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(InputSubType)
class InputSubTypeAdmin(admin.ModelAdmin):
    pass
