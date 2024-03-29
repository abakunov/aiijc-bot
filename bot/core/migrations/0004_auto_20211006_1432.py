# Generated by Django 3.2.8 on 2021-10-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='messages_count_per_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='salary_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='user_tags', to='core.Tag'),
        ),
    ]
