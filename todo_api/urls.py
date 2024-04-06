from django.urls import path, include

from rest_framework.routers import DefaultRouter


from todo_api.views import TodoViewSet, CompletedTask

app_name = 'todo_api'

router = DefaultRouter()
router.register(r'tasks', TodoViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('completed_tasks/', CompletedTask.as_view(), name='completed_tasks'),
]
