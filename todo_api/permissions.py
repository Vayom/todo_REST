from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from django.db import models


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
