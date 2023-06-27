from rest_framework import permissions


class FrontendServerOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the request is coming from the frontend server IP address
        frontend_server_ip = 'X.X.X.X'  # Replace with the actual IP address of the frontend server
        client_ip = request.META.get('REMOTE_ADDR')
        return client_ip == frontend_server_ip