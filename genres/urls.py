from django.urls import path
from . import views #importação relativa, que é quando os dois arquivos estão no mesmo nível e mesma pasta


urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view() , name='genre-create-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view() , name='genre-detail-view'),
]