"""
Module containing views for handling tasks in the todo application.

This module defines views for managing tasks, including creating, updating, deleting, and retrieving tasks.
It also provides views for retrieving completed tasks for the authenticated user.

Classes:
    TodoViewSet: A viewset for handling CRUD operations on tasks belonging to the authenticated user.
    CompletedTask: A view for retrieving a list of completed tasks for the current user.
"""

from django.db.models import QuerySet
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from todo.models import Task
from todo_api.permissions import IsOwner
from todo_api.serializers import TaskSerializer


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


class CompletedTask(generics.ListAPIView):
    """
        View that returns a list of completed tasks for the current user.

        Attributes:
            serializer_class (SerializerClass): The serializer used to serialize task data into JSON format.
            permission_classes (list): A list of permission classes determining whether the current user has access to
            this view.

        Methods:
            get_queryset(self) -> QuerySet[Task]: Returns a queryset of tasks to be displayed in the view.
                Filters tasks based on completion status and the user making the request.

        Example Usage:
            Suppose you have an API for managing tasks. You can use this view to get a list of all completed tasks for
            the current user.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet[Task]:
        """
            Return the queryset of tasks filtered by completion status and the current user.

            Returns:
                QuerySet[Task]: A queryset of tasks filtered by completion status and the current user.

        """
        return Task.objects.filter(completed=True, user=self.request.user)
