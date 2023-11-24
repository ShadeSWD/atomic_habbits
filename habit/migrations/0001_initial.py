# Generated by Django 4.2.7 on 2023-11-24 15:32

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
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='change date')),
                ('place', models.CharField(max_length=50, verbose_name='place of action')),
                ('time', models.TimeField(verbose_name='time of action')),
                ('is_pleasant', models.BooleanField(verbose_name='is pleasant')),
                ('connected_habit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='habit.habit', verbose_name='connected pleasant habit')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'habit',
                'verbose_name_plural': 'habits',
            },
        ),
    ]