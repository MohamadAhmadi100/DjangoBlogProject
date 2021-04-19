from django.urls import path
from .views import user_login, user_register, user_logout

app_name = 'accounts'
urlpatterns = [
    path('login/', user_login, name="user_login"),
    path('register/', user_register, name="user_register"),
    path('logout/', user_logout, name="user_logout"),
]
