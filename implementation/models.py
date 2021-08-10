from django.db import models


class Goal(models.Model):
    goal = models.TextField()
    goal_details = models.TextField()
    goal_after_investment = models.TextField()

    def __str__(self):
        return self.goal

    class Meta:
        db_table = 'tblGoals'
        verbose_name = 'tblGoals'
        verbose_name_plural = 'tblGoals'

class Initiative(models.Model):
    initiative = models.CharField(max_length=200)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE) 
    order = models.PositiveIntegerField(default=0)
    initiative_short_description = models.TextField()

    
    def __str__(self):
        return self.initiative

    class Meta:
        db_table = 'tblInitiatives'
        verbose_name = 'tblInitiatives'
        verbose_name_plural = 'tblInitiatives'
        ordering = ['id']


class InitiativeDetail(models.Model):
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE)
    detail_type = models.ForeignKey('DetailType', on_delete=models.CASCADE)
    initiative_detail = models.TextField()

    def __str__(self):
        return self.initiative_detail

    class Meta:
        db_table = 'tblInitiativeDetails'
        verbose_name = 'tblInitiativeDetails'
        verbose_name_plural = 'tblInitiativeDetails'


class DetailType(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    detail_type = models.CharField(max_length=150)

    def __str__(self):
        return self.detail_type

    class Meta:
        db_table = 'tblListDetailTypes'
        verbose_name = 'tblListDetailTypes'
        verbose_name_plural = 'tblListDetailTypes'


class Output(models.Model):
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE)
    output_type = models.ForeignKey('OutputType', on_delete=models.CASCADE)
    output_text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.initiative

    class Meta:
        db_table = 'tblOuputs'
        verbose_name = 'tblOuputs'
        verbose_name_plural = 'tblOuputs'


class OutputType(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    output_type= models.CharField(max_length=150)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'tblListOuputTypes'
        verbose_name = 'tblListOuputTypes'
        verbose_name_plural = 'tblListOuputTypes'


class Activity(models.Model):
    activity = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE)

    def __str__(self):
        return self.activity

    class Meta:
        db_table = 'tblActivities'
        verbose_name = 'tblActivities'
        verbose_name_plural = 'tblActivities'
        ordering = ['id']


class Input(models.Model):
    input_name = models.CharField(max_length=255)
    input_sub_type = models.ForeignKey('InputSubType', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.input_name

    class Meta:
        db_table = 'tblInputs'
        verbose_name = 'tblInputs'
        verbose_name_plural = 'tblInputs'


class InputType(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    input_type = models.CharField(max_length=100)

    def __str__(self):
        return self.input_type

    class Meta:
        db_table = 'tblListInputTypes'
        verbose_name = 'tblListInputTypes'
        verbose_name_plural = 'tblListInputTypes'


class InputSubType(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    input_sub_type = models.CharField(max_length=100)
    input_type = models.ForeignKey(InputType, on_delete=models.CASCADE)
    units = models.CharField(max_length=100)
    input_sub_type_short = models.CharField(max_length=80)
    units_short = models.CharField(max_length=80)
    cost_usd = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.input_sub_type

    class Meta:
        db_table = 'tblListInputSubTypes'
        verbose_name = 'tblListInputSubTypes'
        verbose_name_plural = 'tblListInputSubTypes'
