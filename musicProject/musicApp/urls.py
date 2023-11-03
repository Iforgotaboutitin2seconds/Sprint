from django.urls import path
from . import views

urlpatterns = [
    path('', views.songListView.as_view(), name='songs'),
    path('song/<int:pk>/', views.songDetailView.as_view(), name='song_detail'),
]
