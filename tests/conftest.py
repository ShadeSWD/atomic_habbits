import pytest
import datetime

from habit.models import Habit
from users.models import User


@pytest.fixture
def user():
    return User.objects.create(username='user', email='testuser@example.com', password='testpassword')


@pytest.fixture
def habit(user):
    return Habit(
        created_at=datetime.datetime.fromisoformat("2023-11-24T20:51:48.333496Z"),
        changed_at=datetime.datetime.fromisoformat("2023-11-24T20:51:48.333496Z"),
        owner=user,
        time=datetime.datetime.fromisoformat("T20:51:48").time(),
        place='testplece',
        action='testaction',
        period=1,
        time_for_action=datetime.datetime.fromisoformat("T00:00:01").time(),
        is_public=1,
        is_pleasant=1,
        connected_habit=None,
        award=None,
    )
