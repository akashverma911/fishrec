from django.urls import path
from . import views
urlpatterns = [
    path('', views.FishListView.as_view(), name='list'),
    path('<int:pk>/', views.FishDetailView.as_view(),name='detail'),
    path('create/', views.FishCreateView.as_view()),
]
