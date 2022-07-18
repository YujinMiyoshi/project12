from django.urls import path
from .views import ToDoList, ToDoListWithPK, ToDoCreate, ToDoDetail, ToDoUpdate, ToDoDelete
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', ToDoList.as_view(), name='todo_list'),
    path('<int:pk>/', ToDoListWithPK.as_view(), name='todo_pk_list'),
    path('create/<int:pk>/', ToDoCreate.as_view(), name='todo_form'),
    path('detail/<int:pk>/', ToDoDetail.as_view(), name='todo_detail'),
    path('update/<int:pk>/', ToDoUpdate.as_view(), name='todo_change'),
    path('delete/<int:pk>/', ToDoDelete.as_view(), name='todo_delete'),
    path('login/', LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]