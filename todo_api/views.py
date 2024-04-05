from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import rest_framework.permissions as permissions

from todo.models import Task
from todo_api.permissions import IsOwner
from todo_api.serializers import TaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling User objects.

    Provides CRUD operations for User objects, including list, retrieve, create,
    update, and delete.

    Attributes:
        serializer_class (UserSerializer): The serializer class used for serializing User objects.
        queryset (QuerySet): The queryset representing all User objects, ordered by date joined.
        permission_classes (list): The list of permission classes applied to this viewset.
            By default, only users with appropriate permissions are allowed to perform operations.

    """
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("-date_joined")
    permission_classes = [permissions.IsAdminUser]


class TodoViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling Task objects related to a user.

    Provides CRUD operations for Task objects that belong to the authenticated user,
    including list, retrieve, create, update, and delete.

    Attributes:
        serializer_class (TaskSerializer): The serializer class used for serializing Task objects.
        permission_classes (list): The list of permission classes applied to this viewset.
            By default, only authenticated users with ownership of the task are allowed to perform operations.

    Methods:
        get_queryset(): Retrieves the queryset of Task objects belonging to the authenticated user.

    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self) -> QuerySet[Task]:
        """
        Retrieves the queryset of Task objects belonging to the authenticated user.

        Returns:
            queryset: A filtered queryset containing Task objects owned by the authenticated user.
        """
        user = self.request.user
        return Task.objects.filter(user=user)
