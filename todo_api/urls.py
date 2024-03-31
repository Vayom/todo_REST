from django.urls import path, include

from rest_framework.routers import DefaultRouter


from todo_api.views import TodoViewSet, UserViewSet

app_name = 'todo_api'

router = DefaultRouter()
router.register(r'tasks', TodoViewSet, basename='task')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
