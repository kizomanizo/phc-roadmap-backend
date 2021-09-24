from django.db import models


class Goal(models.Model):
    name = models.TextField()
    goal_details = models.TextField()
    goal_after_investment = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblGoals'
        verbose_name = 'tblGoals'
        verbose_name_plural = 'tblGoals'


class Initiative(models.Model):
    name = models.CharField(max_length=200)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='initiatives')
    order = models.PositiveIntegerField(default=0)
    initiative_short_description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblInitiatives'
        verbose_name = 'tblInitiatives'
        verbose_name_plural = 'tblInitiatives'
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
        verbose_name = 'tblActivities'
        verbose_name_plural = 'tblActivities'
        ordering = ['id']


class Approach(models.Model):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=100)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name='approach')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblApproaches'
        verbose_name = 'tblApproaches'
        verbose_name_plural = 'tblApproaches'


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
        verbose_name = 'tblInitiativeDetails'
        verbose_name_plural = 'tblInitiativeDetails'


class DetailType(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblListDetailTypes'
        verbose_name = 'tblListDetailTypes'
        verbose_name_plural = 'tblListDetailTypes'


class Output(models.Model):
    initiative = models.ForeignKey(
        Initiative, on_delete=models.CASCADE, related_name='output')
    output_type = models.ForeignKey(
        'OutputType', on_delete=models.CASCADE, related_name='ouput')
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.initiative.name

    class Meta:
        db_table = 'tblOuputs'
        verbose_name = 'tblOuputs'
        verbose_name_plural = 'tblOuputs'


class OutputType(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name= models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblListOuputTypes'
        verbose_name = 'tblListOuputTypes'
        verbose_name_plural = 'tblListOuputTypes'


class InputType(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name='input_types')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblListInputTypes'
        verbose_name = 'tblListInputTypes'
        verbose_name_plural = 'tblListInputTypes'


class Input(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=100)
    input_type = models.ForeignKey(
        InputType, on_delete=models.CASCADE, related_name='inputs')
    units = models.CharField(max_length=100)
    input_short = models.CharField(max_length=80)
    units_short = models.CharField(max_length=80)
    cost_usd = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tblListInputs'
        verbose_name = 'tblListInputs'
        verbose_name_plural = 'tblListInputs'
