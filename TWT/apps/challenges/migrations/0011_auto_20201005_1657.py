# Generated by Django 3.1.1 on 2020-10-05 11:27

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0010_challenge_members_voted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='description',
            field=martor.models.MartorField(help_text='A full description of the challenge.', max_length=2000),
        ),
    ]
