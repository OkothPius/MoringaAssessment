from django.urls import path
from .views import GameListView, GameCreateView, GameUpdateView, GameDeleteView

urlpatterns = [
    path('', GameListView.as_view(), name='home'),
    path('new/', GameCreateView.as_view(), name='game-create'),
    path('game/<int:pk>/update/', GameUpdateView.as_view(), name='game-update'),
    path('game/<int:pk>/delete/', GameDeleteView.as_view(), name='game-delete'),

]
