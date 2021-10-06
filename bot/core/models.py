from django.db import models

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

    custom_position = models.CharField(max_length=100)
    operating_schedule = models.CharField(max_length=1000, default='')
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    description = models.TextField()
    offer_education = models.CharField(max_length=1000, default='')
    offer_experience_year_count = models.IntegerField()
    city_id = models.IntegerField()
    is_male = models.BooleanField()


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class User(models.Model):
    tg_id = models.IntegerField(default=0)
    username = models.CharField(max_length=200, default='')
    city_id = models.IntegerField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='user_tags', blank=True)
    salary_from = models.IntegerField(blank=True, null=True)
    messages_count_per_day = models.IntegerField(blank=True, null=True)
    link = models.URLField(max_length = 200, default='')