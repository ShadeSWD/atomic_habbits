import os
from celery import shared_task
import requests
from habit.models import Habit
from datetime import datetime, timedelta


@shared_task
def send_message():
    current_time = datetime.now().time()
    current_day = datetime.now().date()

    habits = Habit.objects.all()

    for habit in habits:
        habit_time = habit.time
        if habit.period == 0:
            is_active = True
        elif ((current_day - habit.created_at.date()) % timedelta(days=habit.period)).days == 0:
            is_active = True
        else:
            is_active = False

        if is_active and current_time == habit_time:
            message = str(habit)

            chat_id = habit.user.telegram_id
            url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_API_TOKEN')}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(url).json()
