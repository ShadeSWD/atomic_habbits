from rest_framework import viewsets
from habit.models import Habit
from habit.serializers import HabitSerializer
from habit.paginators import HabitPagination
from habit.permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsOwner, ]
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        new = serializer.save()
        new.owner = self.request.user
        new.save()
