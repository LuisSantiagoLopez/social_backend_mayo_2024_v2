from rest_framework import permissions 


class IsReservationOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow modification if the user is the owner of the reservation or the owner of the associated antro
        return obj.user == request.user or obj.antro.user == request.user

class IsReservationItemOwnerOrAntroOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow modification if the user is the owner of the reservation or the owner of the associated antro
        return obj.reservation.user == request.user or obj.reservation.antro.user == request.user
