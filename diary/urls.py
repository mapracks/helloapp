from django.urls import path
from .views import EntryDetailView ,EntryCreateView,EntryUpdateView,EntryDeleteView
from . import views



urlpatterns = [
    path('' , views.cover , name = 'cover'),
    path('profile/' , views.Profile , name = 'Profile'),
    path('home/', views.home , name = 'homepage'),
    path('description/<int:pk>/', EntryDetailView.as_view() , name = 'description'),
    path('add/', EntryCreateView.as_view() , name = 'add'),
    path('description/<int:pk>/update/', EntryUpdateView.as_view() , name = 'update'),
    path('description/<int:pk>/delete/', EntryDeleteView.as_view() , name = 'delete'),
    path('register/', views.register , name = 'register')
]