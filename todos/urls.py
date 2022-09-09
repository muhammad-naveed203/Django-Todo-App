from django.urls import path

from .views import TodoListView, TodoPublic, MyPublic, ItemListView, ItemDetail, ListDetail

urlpatterns = [

    path('todo/', TodoListView.as_view()),
    path('todo/<int:pk>/', ListDetail.as_view()),
    path('pub_todos/', TodoPublic.as_view()),
    path('my_public/', MyPublic.as_view()),
    path('item/', ItemListView.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),

]
