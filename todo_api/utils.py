from datetime import timezone

from django.contrib.auth.models import User

from todo.models import Task


class TaskFake(Task):
    user = User.objects.get(username='fakeuser')
    title = 'FakeTittle'
    description = 'FakeDescription'
    completed = False
    created_at = timezone.now()
    updated_at = timezone.now()
