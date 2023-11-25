import pytest

from habit.models import Habit


@pytest.mark.django_db
def test_habit_model(habit):
    habit.save()
    retrieved_habit = Habit.objects.get(pk=1)

    assert retrieved_habit.user == habit.user
    assert retrieved_habit.place == "testplace"


@pytest.mark.django_db
def test_habit_str_method(habit):
    str_representation = str(habit)
    assert str_representation == f'I will testaction at 20:51:48 at testplace'
