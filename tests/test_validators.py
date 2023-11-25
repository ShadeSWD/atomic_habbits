import datetime

import pytest
from habit.validators import (
    validate_award,
    validate_frequency,
    validate_time_for_action,
)
from rest_framework.exceptions import ValidationError


def test_validate_related_habit():
    valid_data = {'connected_habit': None, 'award': ''}
    validate_award(valid_data)

    invalid_data = {'connected_habit': 1, 'award': 'award'}
    with pytest.raises(ValidationError):
        validate_award(invalid_data)


def test_validate_frequency():
    valid_data = 2
    invalid_data = 12
    assert validate_frequency(valid_data)
    with pytest.raises(ValidationError):
        validate_frequency(invalid_data)


def test_validate_time_for_action():
    valid_data = datetime.datetime.fromisoformat("T00:00:01").time()
    invalid_data = datetime.datetime.fromisoformat("T00:50:01").time()
    assert validate_time_for_action(valid_data)
    with pytest.raises(ValidationError):
        validate_time_for_action(invalid_data)
