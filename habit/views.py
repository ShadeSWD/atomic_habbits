from rest_framework import viewsets
from habit.models import Habit
from habit.serializers import HabitSerializer
from habit.paginators import HabitPagination


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    queryset = Habit.objects.all()
