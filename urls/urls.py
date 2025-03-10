from django.urls import path
from .views import CreateURLView, UserLinkListView, SharedUserLinkListView, UpdateURLView, DeleteURLView, RetrieveOriginalURL

urlpatterns = [
    path('create-link', CreateURLView.as_view(), name='create-link'),
    path('user-links', UserLinkListView.as_view(), name='user-links'),
    path('user-links/<int:user_id>', SharedUserLinkListView.as_view(), name='shared-user-links'),
    path("update-link/<int:pk>", UpdateURLView.as_view(), name="update-url"),
    path("delete-link/<int:pk>", DeleteURLView.as_view(), name="delete-url"),
    path("urls/<int:user_id>/<str:short_url>/", RetrieveOriginalURL.as_view(), name='retrieve-original-url')
]
