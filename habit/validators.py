from datetime import timedelta
from rest_framework import serializers


def validate_award(value):
    if value['connected_habit'] and value['award']:
        raise serializers.ValidationError("You can't choose both a related habit and a reward.")

    if value['is_pleasant'] and (value['award'] or value['connected_habit']):
        raise serializers.ValidationError("A pleasant habit should not have a reward or a related habit.")

    if value['connected_habit']:
        if not value['connected_habit'].is_pleasant:
            raise serializers.ValidationError("Related habit should be pleasant.")


def validate_frequency(value):
    if value['period'] not in [i for i in range(1, 8)]:
        raise serializers.ValidationError("The minimum frequency is once in 7 days for non-daily habits.")


def validate_time_for_action(value):
    if value['time_for_action'] > timedelta(minutes=2):
        raise serializers.ValidationError("Estimated time should not exceed 120 seconds.")
