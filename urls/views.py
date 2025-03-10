from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .serializer import URLSerializer
from .models import URL


class CreateURLView(generics.CreateAPIView):
    serializer_class = URLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UserLinkListView(generics.ListAPIView):
    serializer_class = URLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return URL.objects.filter(created_by=self.request.user)


class SharedUserLinkListView(generics.ListAPIView):
    serializer_class = URLSerializer
    authentication_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return URL.objects.filter(created_by=user_id)


#  Update URL (Only the owner can update)
class UpdateURLView(generics.RetrieveUpdateAPIView):
    serializer_class = URLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return URL.objects.filter(created_by=self.request.user)


#  Delete URL (Only the owner can delete)
class DeleteURLView(generics.DestroyAPIView):
    serializer_class = URLSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return URL.objects.filter(created_by=self.request.user)


class RetrieveOriginalURL(generics.RetrieveAPIView):
    serializer_class = URLSerializer
    permission_classes = []  # Allow public access

    def get_queryset(self):
        """Query by short URL without requiring authentication"""
        short_url = self.kwargs["short_url"]
        user_id = self.kwargs["user_id"]
        return URL.objects.filter(short_url=short_url, created_by__id=user_id,)

    def get_object(self):
        """Retrieve the URL object or return 404"""
        queryset = self.get_queryset()
        return get_object_or_404(queryset)
# Create your views here.
