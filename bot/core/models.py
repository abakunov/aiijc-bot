from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Position(models.Model):

    OPERATING_SCHEDULE_ID_VALUES = (
        (1, 'Полный рабочий день'),
        (2, 'Свободный график'),
        (3, 'Сменный график'),
        (5, 'Частичная занятость'),
        (6, 'Удаленная работа'),
        (7, 'Вахта'),
        (-100, 'Не указано'),
    )

    #todo
    OFFER_EDUCATION_ID_VALUES = (
        (0, 'Любое'),
        (1, 'Среднее'),
        (2, 'Среднее профессиональное'),
        (3, 'Неполное высшее'),
        (4, 'Высшее'),
    )

    custom_position = models.CharField(max_length=100, blank=True, null=True)
    operating_schedule = models.CharField(max_length=1000, default='', blank=True, null=True)
    salary_from = models.IntegerField(blank=True, null=True)
    salary_to = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    offer_education = models.CharField(max_length=1000, default='', blank=True, null=True)
    offer_experience_year_count = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    is_male = models.BooleanField(blank=True, null=True)
    link = models.URLField(max_length = 200, default='', blank=True, null=True)
    predicted_tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=1, blank=True, null=True)


class User(models.Model):
    tg_id = models.IntegerField(default=0)
    username = models.CharField(max_length=200, default='')
    city_id = models.IntegerField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='user_tags', blank=True)
    salary_from = models.IntegerField(blank=True, null=True)
    messages_count_per_day = models.IntegerField(blank=True, null=True)