from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from djoser.views import UserViewSet
from apps.users.pagination import UserPagination


class CustomUsersViewSet(UserViewSet):

    pagination_class = UserPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ["is_active", "is_staff", "is_superuser", "username", "email"]
    search_fields = ["username", "email", "first_name", "last_name"]
    ordering_fields = ["date_joined"]
    ordering = ["date_joined"]

    lookup_field = "id"
    lookup_url_kwarg = "id"