from rest_framework.permissions import BasePermission
from .models import CustomUser


class IsOwner(BasePermission):
    """Custom permission class to allow bucketlist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, CustomUser):
            return obj == request.user
        return obj == request.user