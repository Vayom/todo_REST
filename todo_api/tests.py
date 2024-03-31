"""
Module: test_task_view_set_api.py

This module contains unit tests for the TaskViewSet API endpoints.

Test Cases:
    - TestTaskViewSetApi(APITestCase): A test case class for testing TaskViewSet API endpoints.

"""

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from todo.models import Task


class TestTaskViewSetApi(APITestCase):
    """
    Test case class for testing TaskViewSet API endpoints.

    Attributes:
        user (User): A test user object created for authentication.
        access_token (AccessToken): Access token generated for the test user.
        task1 (Task): A test task object created and assigned to the test user.
        task2 (Task): A test task object created without user assignment.
    """

    def setUp(self):
        """
        Set up test data.

        Creates a test user, access token, and test tasks for each test method.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.access_token = AccessToken.for_user(self.user)
        self.task1 = Task.objects.create(title='fakeName', description='fakeDescription', user=self.user)
        self.task2 = Task.objects.create(title='fakeName2', description='fakeDescription2', user=None)

    def test_list_tasks_authenticated(self):
        """
        Test listing tasks when authenticated.

        Ensures that only tasks assigned to the authenticated user are listed.
        """
        # JWT-token auth
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get('/api/v1/tasks/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_tasks_unauthenticated(self):
        """
        Test listing tasks when unauthenticated.

        Ensures that an unauthenticated request returns unauthorized status.
        """
        response = self.client.get('/api/v1/tasks/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_current_task(self):
        """
        Test retrieving a specific task.

        Ensures that a task is retrieved if it belongs to the authenticated user,
        and a 404 is returned if the task does not exist or does not belong to the user.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        response = self.client.get('http://127.0.0.1:8000/api/v1/tasks/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('http://127.0.0.1:8000/api/v1/tasks/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_current_task_unauthenticated(self):
        """
        Test retrieving a specific task when unauthenticated.

        Ensures that unauthenticated requests for specific tasks return unauthorized status.
        """
        response = self.client.get('http://127.0.0.1:8000/api/v1/tasks/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get('http://127.0.0.1:8000/api/v1/tasks/2/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_task(self):
        """
        Test updating a task.

        Ensures that a task can be updated if it belongs to the authenticated user,
        and a 404 is returned if the task does not exist or does not belong to the user.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        response = self.client.put('http://127.0.0.1:8000/api/v1/tasks/1/',
                                   data={'title': 'put_title',
                                         'description': 'put_description'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put('http://127.0.0.1:8000/api/v1/tasks/2/',
                                   data={'title': 'put_title',
                                         'description': 'put_description'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_task(self):
        """
        Test deleting a task.

        Ensures that a task can be deleted if it belongs to the authenticated user,
        and a 404 is returned if the task does not exist or does not belong to the user.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        response = self.client.delete('http://127.0.0.1:8000/api/v1/tasks/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('http://127.0.0.1:8000/api/v1/tasks/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
