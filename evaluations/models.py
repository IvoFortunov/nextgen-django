from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
import uuid
import datetime

class WeeklyEvaluation(models.Model):
    MARKS = [(i,i) for i in range(1,6)]
    MARKS.insert(0,('','-----'))
    YEARS = [(i,i) for i in range(2023,2033)]
    WEEKS = [(i,i) for i in range(1,58)]
    currentYear = datetime.datetime.now().year
    currentWeek = datetime.datetime.now().isocalendar()[1]
    topic = models.CharField(max_length=200, null=True)
    player = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL, related_name='player')
    coach = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='coach')
    year = models.IntegerField(choices = YEARS, default=currentYear)
    week = models.IntegerField(choices = WEEKS, default=currentWeek)
    player_motivation = models.IntegerField(null=True, blank=True,choices = MARKS)
    coach_motivation = models.IntegerField(null=True, blank=True,choices = MARKS)
    player_concentration = models.IntegerField(null=True, blank=True,choices = MARKS)
    coach_concentration = models.IntegerField(null=True, blank=True,choices = MARKS)
    player_discipline = models.IntegerField(null=True, blank=True,choices = MARKS)
    coach_discipline = models.IntegerField(null=True, blank=True,choices = MARKS)
    player_effort = models.IntegerField(null=True, blank=True,choices = MARKS)
    coach_effort = models.IntegerField(null=True, blank=True,choices = MARKS)
    player_understanding = models.IntegerField(null=True, blank=True,choices = MARKS)
    coach_understanding = models.IntegerField(null=True, blank=True,choices = MARKS)
    player_feedback = models.TextField(null=True, blank= True)
    coach_feedback = models.TextField(null=True, blank= True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        ordering = ['-year', '-week', 'player__name']
        unique_together = ('player', 'week', 'year')

    def __str__(self)->str:
        coachName = ''
        if(self.coach):
            coachName = self.coach.name
        return str(self.player.name + ', Седмица: ' + str(self.week) + ', Година: ' + str(self.year) + ', Треньор: ' + coachName)
    

class CommonEvaluation(models.Model):
    MARKS = [(i,i) for i in range(1,11)]
    MARKS.insert(0,('','-----'))
    WIN_CHOICES=(('W', 'Завършващи удари'),('E', 'Грешки на противника'))
    player = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL)
    style = models.TextField(null=True, blank= True)

    quality_forehand = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_backhand = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_first_serve = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_second_serve = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_receive_first_serve = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_receive_second_serve = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_forehand_volley = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_backhand_volley = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_smash = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_forehand_lob = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_backhand_lob = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_drop_shot = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_forehand_topspin = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_backhand_topspin = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_forehand_slice = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_backhand_slice = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_forehand_passing_shot = models.IntegerField(null=True, blank=True,choices = MARKS)
    quality_backhand_passing_shot = models.IntegerField(null=True, blank=True,choices = MARKS)

    best_shot = models.CharField(max_length=200, null=True, blank=True)
    best_shot_for_winner = models.CharField(max_length=200, null=True, blank=True)
    shot_improved = models.CharField(max_length=200, null=True, blank=True)
    more_points_won = models.CharField(max_length=10, choices = WIN_CHOICES, default = "E")

    technical = models.IntegerField(null=True, blank=True,choices = MARKS)
    tactical = models.IntegerField(null=True, blank=True,choices = MARKS)
    mental = models.IntegerField(null=True, blank=True,choices = MARKS)
    condition = models.IntegerField(null=True, blank=True,choices = MARKS)

    serve = models.IntegerField(null=True, blank=True,choices = MARKS)
    receiving = models.IntegerField(null=True, blank=True,choices = MARKS)
    base_line = models.IntegerField(null=True, blank=True,choices = MARKS)
    net = models.IntegerField(null=True, blank=True,choices = MARKS)

    strength = models.IntegerField(null=True, blank=True,choices = MARKS)
    speed = models.IntegerField(null=True, blank=True,choices = MARKS)
    endurance = models.IntegerField(null=True, blank=True,choices = MARKS)
    agility = models.IntegerField(null=True, blank=True,choices = MARKS)

    concentration = models.IntegerField(null=True, blank=True,choices = MARKS)
    error_handling = models.IntegerField(null=True, blank=True,choices = MARKS)
    effort = models.IntegerField(null=True, blank=True,choices = MARKS)
    pleasure = models.IntegerField(null=True, blank=True,choices = MARKS)
    skill = models.IntegerField(null=True, blank=True,choices = MARKS)
    mental_stabillity = models.IntegerField(null=True, blank=True,choices = MARKS)
    confidence = models.IntegerField(null=True, blank=True,choices = MARKS)

    style_change = models.IntegerField(null=True, blank=True,choices = MARKS)
    attack = models.IntegerField(null=True, blank=True,choices = MARKS)
    defence = models.IntegerField(null=True, blank=True,choices = MARKS)
    delay = models.IntegerField(null=True, blank=True,choices = MARKS)
    break_rhythm = models.IntegerField(null=True, blank=True,choices = MARKS)
    speedup = models.IntegerField(null=True, blank=True,choices = MARKS)
    sence = models.IntegerField(null=True, blank=True,choices = MARKS)

    short_term_goal_technical = models.CharField(max_length=500, null=True, blank=True)
    short_term_goal_tactical = models.CharField(max_length=500, null=True, blank=True)
    short_term_goal_physical = models.CharField(max_length=500, null=True, blank=True)
    short_term_goal_competition = models.CharField(max_length=500, null=True, blank=True)

    long_term_goal_technical = models.CharField(max_length=500, null=True, blank=True)
    long_term_goal_tactical = models.CharField(max_length=500, null=True, blank=True)
    long_term_goal_physical = models.CharField(max_length=500, null=True, blank=True)
    long_term_goal_competition = models.CharField(max_length=500, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        ordering = ['player__name', '-created']

    def __str__(self)->str:
        return str(self.player.name + ', Дата: ' + str(self.created.date()))
    

class MatchEvaluation(models.Model):
    MATCHTYPE = (('S', 'Спаринг'),('T', 'Турнир'))
    ROUNDS = (('Q1', 'Квалификация 1 кръг'), ('Q2', 'Квалификация 2 кръг'), ('Q1', 'Квалификация 3 кръг'),
              ('R1', '1 кръг'),('R2', '2 кръг'),('R3', '3 кръг'),('QF', 'Четвъртфинал'),('SF', 'Полуфинал'),('F', 'Финал'),('NO', 'Няма'))
    WINLOOSE = (('W', 'Победа'),('L', 'Загуба'))

    
    player = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL)
    matchtype = models.CharField(max_length=10, choices = MATCHTYPE, default = "S")
    tournament = models.CharField(max_length=200, null=True, blank= True)
    round = models.CharField(max_length=10, choices = ROUNDS, default = "NO")
    opponent = models.CharField(max_length=200, null=True, blank= True)
    winloose = models.CharField(max_length=10, choices = WINLOOSE, default = "W")
    result = models.CharField(max_length=200, null=True)
    comments = models.TextField(null=True, blank= True)
    coachVisible = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        ordering = ['player__name', '-created', ]

    def __str__(self)->str:
        return str(self.player.name + ', с/у: ' + str(self.opponent) + ', Резултат: ' + str(self.result) + ', Дата: ' + str(self.created.date()))
    

class DailyEvaluation(models.Model):
    PRACTICEHTYPE = (('S', 'Индивидуална'),('G', 'Групова'))
    MARKS = [(i,i) for i in range(1,6)]
    MARKS.insert(0,('','-----'))

    player = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL, related_name='playerdaily')
    coach = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='coachdaily')

    date = models.DateField(null=True, default=datetime.datetime.today)
    mark = models.IntegerField(null=True,choices = MARKS)
    practicetype = models.CharField(max_length=10, choices = PRACTICEHTYPE, default = "G")
    comments = models.TextField(null=True, blank= True)
    coachVisible = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        ordering = ['-date', '-created']

    def __str__(self)->str:
        return str(self.player.name + ', Дата: ' + str(self.date))
    

class ConditioningEvaluation(models.Model):
    MARKS = [(i,i) for i in range(1,6)]
    MARKS.insert(0,('','-'))
    YEARS = [(i,i) for i in range(2023,2033)]
    WEEKS = [(i,i) for i in range(1,58)]
    currentYear = datetime.datetime.now().year
    currentWeek = datetime.datetime.now().isocalendar()[1]
    player = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL, related_name='playerconditioning')
    coach = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='coachconditioning')
    year = models.IntegerField(choices = YEARS, default=currentYear)
    week = models.IntegerField(choices = WEEKS, default=currentWeek)
    mon_practice = models.IntegerField(null=True, blank=True,choices = MARKS)
    mon_concentration = models.IntegerField(null=True, blank=True,choices = MARKS)
    mon_sleep = models.IntegerField(null=True, blank=True,choices = MARKS)
    mon_diet = models.IntegerField(null=True, blank=True,choices = MARKS)
    mon_recovery = models.IntegerField(null=True, blank=True,choices = MARKS)
    tue_practice = models.IntegerField(null=True, blank=True,choices = MARKS)
    tue_concentration = models.IntegerField(null=True, blank=True,choices = MARKS)
    tue_sleep = models.IntegerField(null=True, blank=True,choices = MARKS)
    tue_diet = models.IntegerField(null=True, blank=True,choices = MARKS)
    tue_recovery = models.IntegerField(null=True, blank=True,choices = MARKS)
    wed_practice = models.IntegerField(null=True, blank=True,choices = MARKS)
    wed_concentration = models.IntegerField(null=True, blank=True,choices = MARKS)
    wed_sleep = models.IntegerField(null=True, blank=True,choices = MARKS)
    wed_diet = models.IntegerField(null=True, blank=True,choices = MARKS)
    wed_recovery = models.IntegerField(null=True, blank=True,choices = MARKS)
    thu_practice = models.IntegerField(null=True, blank=True,choices = MARKS)
    thu_concentration = models.IntegerField(null=True, blank=True,choices = MARKS)
    thu_sleep = models.IntegerField(null=True, blank=True,choices = MARKS)
    thu_diet = models.IntegerField(null=True, blank=True,choices = MARKS)
    thu_recovery = models.IntegerField(null=True, blank=True,choices = MARKS)
    fri_practice = models.IntegerField(null=True, blank=True,choices = MARKS)
    fri_concentration = models.IntegerField(null=True, blank=True,choices = MARKS)
    fri_sleep = models.IntegerField(null=True, blank=True,choices = MARKS)
    fri_diet = models.IntegerField(null=True, blank=True,choices = MARKS)
    fri_recovery = models.IntegerField(null=True, blank=True,choices = MARKS)
    sat_practice = models.IntegerField(null=True, blank=True,choices = MARKS)
    sat_concentration = models.IntegerField(null=True, blank=True,choices = MARKS)
    sat_sleep = models.IntegerField(null=True, blank=True,choices = MARKS)
    sat_diet = models.IntegerField(null=True, blank=True,choices = MARKS)
    sat_recovery = models.IntegerField(null=True, blank=True,choices = MARKS)
    sun_practice = models.IntegerField(null=True, blank=True,choices = MARKS)
    sun_concentration = models.IntegerField(null=True, blank=True,choices = MARKS)
    sun_sleep = models.IntegerField(null=True, blank=True,choices = MARKS)
    sun_diet = models.IntegerField(null=True, blank=True,choices = MARKS)
    sun_recovery = models.IntegerField(null=True, blank=True,choices = MARKS)
    average = models.FloatField(null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        ordering = ['-year', '-week', 'player__name']
        unique_together = ('player', 'week', 'year')

    def __str__(self)->str:
        coachName = ''
        if(self.coach):
            coachName = self.coach.name
        return str(self.player.name + ', Седмица: ' + str(self.week) + ', Година: ' + str(self.year) + ', Треньор: ' + coachName)
