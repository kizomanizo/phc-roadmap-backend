from django.db import models


class Goal(models.Model):
    name = models.TextField()
    goal_details = models.TextField()
    goal_after_investment = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblGoals'


class Initiative(models.Model):
    name = models.CharField(max_length=200)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='initiatives')
    order = models.PositiveIntegerField(default=0)
    initiative_short_description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblInitiatives'
        ordering = ['id']


class Activity(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    initiative = models.ForeignKey(
        Initiative, on_delete=models.CASCADE, related_name='activities')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblActivities'
        verbose_name_plural = 'Activities'
        ordering = ['id']


class InputType(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblInputTypes'
        verbose_name_plural = 'Input Types'
        ordering = ['id']


class InputSubType(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=100)
    input_type = models.ForeignKey(
        InputType, on_delete=models.CASCADE, related_name='input_sub_types')
    units = models.CharField(max_length=100)
    input_sub_type_short = models.CharField(max_length=80)
    units_short = models.CharField(max_length=80)
    cost_usd = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblInputSubTypes'
        verbose_name_plural = 'Input Subtypes'


class Input(models.Model):
    name = models.CharField(max_length=255)
    input_sub_type = models.ForeignKey(
        InputSubType,
        on_delete=models.CASCADE,
        related_name='inputs',
        verbose_name='Input Subtype'
    )
    quantity = models.PositiveIntegerField(default=0)
    notes = models.CharField(max_length=100)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name='inputs')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblInputs'
        ordering = ['id']


class InitiativeDetail(models.Model):
    initiative = models.ForeignKey(
        Initiative, on_delete=models.CASCADE, related_name='initiative_details')
    detail_type = models.ForeignKey(
        'DetailType', on_delete=models.CASCADE, related_name='initiative_details')
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'tblInitiativeDetails'
        verbose_name_plural = 'Initiative Details'
        ordering = ['id']


class DetailType(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblListDetailTypes'
        verbose_name_plural = 'Detail Types'


class Output(models.Model):
    initiative = models.ForeignKey(
        Initiative, on_delete=models.CASCADE, related_name='outputs')
    output_type = models.ForeignKey(
        'OutputType', on_delete=models.CASCADE, related_name='ouputs')
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.initiative.name

    class Meta:
        db_table = 'tblOuputs'
        ordering = ['id']


class OutputType(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name= models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblOuputTypes'
        verbose_name_plural = 'Output Types'
