from django.urls import path
from .views import SignUpView, LoginView, UserUpdateView, UserDetailsView, UserDetailByIdView

urlpatterns = [
    path('register', SignUpView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('update-user', UserUpdateView.as_view(), name='update-user'),
    path('users', UserDetailsView.as_view(), name='user-details'),
    path('user/<int:user_id>', UserDetailByIdView.as_view(), name='user-detail-by-id'),

]
