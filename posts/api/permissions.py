from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,req,view,obj):
        if req.method in permissions.SAFE_METHODS:
            return True
        return obj.author == req.user
