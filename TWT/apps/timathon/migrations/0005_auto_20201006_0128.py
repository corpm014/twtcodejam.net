# Generated by Django 3.1.1 on 2020-10-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timathon', '0004_team_voted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='winner',
        ),
        migrations.AddField(
            model_name='team',
            name='winner_position',
            field=models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third')], default=0),
        ),
    ]
