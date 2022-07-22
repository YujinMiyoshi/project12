from django.urls import path
from .views import Login, Logout, UserCreate, UserCreateDone, UserCreateComplete

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('login/user_create/', UserCreate.as_view(), name='user_create'),
    path('login/user_create/done/', UserCreateDone.as_view(), name='user_create_done'),
    path('login/user_create/complete/<token>/', UserCreateComplete.as_view(), name='user_create_complete'),
]