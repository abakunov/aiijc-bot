# Generated by Django 3.2.8 on 2021-10-06 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_position', models.CharField(max_length=100)),
                ('operating_schedule_id', models.IntegerField()),
                ('salary_from', models.IntegerField()),
                ('salary_to', models.IntegerField()),
                ('description', models.TextField()),
                ('offer_education_id', models.IntegerField()),
                ('offer_experience_year_count', models.IntegerField()),
                ('city_id', models.IntegerField()),
                ('is_male', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.IntegerField()),
                ('salary_from', models.IntegerField()),
                ('messages_count_per_day', models.IntegerField()),
                ('tags', models.ManyToManyField(related_name='user_tags', to='core.Tag')),
            ],
        ),
    ]