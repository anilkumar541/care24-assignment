from rest_framework import permissions

class IsAuthorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # print("checking only permmission", request.user.admin)
        if view.action == 'list' and not request.user.is_authenticated:
            return True

        if not request.user.is_authenticated:
            return False
        
        if view.action == 'create' and request.user.admin and request.user:
            return False
       
        return True


    def has_object_permission(self, request, view, obj):
        print("checking only obj_permmission")
        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser or request.user.admin:
            return True

        if view.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return obj.author == request.user

    def has_view_permission(self, request, view):
        
        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser or request.user.admin:
            return True

        if view.action == 'list':
            return True

        return False
        




"""
In the above code, the has_permission method checks if the user making the request is authenticated. If the user is not authenticated (i.e., not logged in), it will return False, indicating that the user does not have permission to perform the action. This will prevent users who are not logged in from creating any records."""        

