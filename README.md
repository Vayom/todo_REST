# REST Todo Проект

Этот репозиторий содержит проект Django, который реализует RESTful API для управления списком задач (TODO). Проект также включает в себя систему разделения по ролям пользователей.

## Особенности

- Реализация RESTful API для управления задачами (CRUD операции).
- Разделение по ролям: аутентифицированные пользователи могут создавать, изменять и удалять свои задачи, а администраторы имеют доступ ко всем задачам.
- Использование Docker и Docker Compose для легкого развертывания и управления окружением проекта.

- Использование
После успешного запуска Docker Compose, вы можете получить доступ к API по адресу http://http://127.0.0.1:8000. Документация API доступна по адресу http://127.0.0.1:8000/docs/.
Также доступен URL http://127.0.0.1:8000/api/schema/swagger-ui/

Аутентификация - http://127.0.0.1:8000/api-auth/login/
Получение своих задач или создание новой - http://127.0.0.1:8000/api/v1/tasks/
Получение, редактирование или удаление своей задачи - http://127.0.0.1:8000/api/v1/tasks/<int:pk>

Структура проекта
todoREST/: 
/todo - приложение, которое хранит модели и миграции базы данных
/todo_api - приложение для реализации view и permission
