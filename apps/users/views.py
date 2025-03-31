from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework import status

from apps.users.pagination import UserPagination


User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
           
            email = request.data.get("email")
            try:
                user = User.objects.get(email=email)
                if user.is_locked:
                    return Response(
                        {
                            "error": "Account is locked due to too many failed login attempts."
                        },
                        status=status.HTTP_403_FORBIDDEN,
                    )
                user.failed_login_attempts = 0
                user.save()
            except User.DoesNotExist:
                pass 
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
           
            email = request.data.get("email")
            try:
                user = User.objects.get(email=email)
                user.failed_login_attempts += 1
                if user.failed_login_attempts >= 3:
                    user.is_locked = True
                user.save()
            except User.DoesNotExist:
                pass 

        return response


class CustomTokenRefreshView(TokenRefreshView):
    pass


class CustomTokenVerifyView(TokenVerifyView):
    pass


class CustomUsersViewSet(UserViewSet):

    pagination_class = UserPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["is_active", "is_staff", "is_superuser", "username", "email"]
    search_fields = ["username", "email", "first_name", "last_name"]
    ordering_fields = ["date_joined"]
    ordering = ["date_joined"]

    lookup_field = "id"
    lookup_url_kwarg = "id"
