from rest_framework import serializers
from habit.models import Habit
from habit.validators import *


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        validate_award(data)
        validate_frequency(data)
        validate_time_for_action(data)
        return data
