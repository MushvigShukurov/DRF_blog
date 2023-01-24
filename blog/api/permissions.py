from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin =  super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin



# Commenti ancaq sahibi uUpDel ede biler
class IsOwnerOfCommentOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
    