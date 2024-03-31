from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Model representing tasks in a to-do list application.

    Attributes:
        user (ForeignKey): A foreign key to the User model from django.contrib.auth.models.
            Represents the user who created the task. Can be blank or null.
        title (CharField): The title of the task, limited to 100 characters.
        description (TextField): Description of the task. Can be blank or null.
        completed (BooleanField): A boolean field indicating whether the task is completed or not. Default is False.
        created_at (DateTimeField): A field storing the date and time when the task was created.
            Automatically set when a new task object is created.
        updated_at (DateTimeField): A field storing the date and time when the task was last updated.
            Automatically updated whenever the task object is modified.

    Methods:hehe
        __str__(): Returns the string representation of the task object, which is its title.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the string representation of the task object.

        Returns:
            str: The title of the task.
        """
        return self.title
