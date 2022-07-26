# Generated by Django 4.0.2 on 2022-04-08 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('for_members', models.BooleanField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('questions', models.ManyToManyField(to='questionnaire.Question')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField()),
                ('full_details', models.TextField(null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='questionnaire.question')),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_conditions', models.TextField(null=True)),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='questionnaire.questionnaire')),
                ('response', models.ManyToManyField(to='questionnaire.ResponseOption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
