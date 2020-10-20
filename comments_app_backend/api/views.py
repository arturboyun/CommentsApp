from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import controllers
from .models import Comment
from .pagination import CustomPageNumberPagination
from .permissions import IsAdminOrReadCreateOnly
from .serializers import CommentSerializer, CommentCreateSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadCreateOnly]
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['username', 'email', 'home_page']
    search_fields = ['text', 'username', 'email', 'home_page', 'created_at']
    ordering_fields = ['username', 'email', 'home_page', 'created_at', 'modifed_at']

    def create(self, request, *args, **kwargs):
        serializer = CommentCreateSerializer(data=request.data)
        ip = controllers.get_client_ip(request)
        browser_info = controllers.get_browser_info(request)
        request.data.update({'ip': ip, 'browser_info': browser_info})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Comment.objects.filter(reply_to=None))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)