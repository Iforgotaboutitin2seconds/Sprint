from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('songs/', views.SongListView.as_view(), name='songs'),
    path('song/<int:pk>/', views.SongDetailView.as_view(), name='song_detail'),
    path('song/new/', views.SongCreateView.as_view(), name='song_new'),
    path('song/<int:pk>/edit/', views.SongUpdateView.as_view(), name='song_edit'),
    path('song/<int:pk>/delete/', views.SongDeleteView.as_view(), name='song_delete'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('about/', views.AboutView.as_view(), name='about'),
]
