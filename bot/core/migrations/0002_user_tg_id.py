# Generated by Django 3.2.8 on 2021-10-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_id',
            field=models.IntegerField(default=0),
        ),
    ]
