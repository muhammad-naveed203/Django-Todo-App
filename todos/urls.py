from django.urls import path

from .views import TodoListView, TodoPublic, ItemListView, ItemDetail

urlpatterns = [

    path('todo/', TodoListView.as_view()),
    path('pub_todos/', TodoPublic.as_view()),
    path('item/', ItemListView.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),

]
