from django.urls import path
from django.contrib.auth import views
from . import views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('', views.index, name="index"),
    path('songs/', views.songListView.as_view(), name='songs'),
    path('song/<int:pk>/', views.songDetailView.as_view(), name='song_detail'),
    path('song/new/', views.songCreateView.as_view(), name='song_new'),
    path('song/<int:pk>/edit/', views.songUpdateView.as_view(), name='song_edit'),
    path('song/<int:pk>/delete/', views.songDeleteView.as_view(), name='song_delete'),
    path('login/', views.loginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.registerView.as_view(), name='register'),
    path('about/', views.aboutView.as_view(), name='about'),
]
