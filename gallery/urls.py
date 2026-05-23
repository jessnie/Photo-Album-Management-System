from django.urls import path
from . import views

urlpatterns = [
    # Gallery URLs
    path('', views.GalleryListView.as_view(), name='gallery_home'),
    path('photo/<int:pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/create/', views.PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/edit/', views.PhotoUpdateView.as_view(), name='photo_edit'),
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('my-photos/', views.UserPhotosView.as_view(), name='user_photos'),
    
    # Legacy URLs (for backwards compatibility)
    path('recipe/<int:pk>/edit/', views.PhotoUpdateView.as_view(), name='edit_recipe'),
    path('recipe/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='delete_recipe'),
    
    # Authentication URLs
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

