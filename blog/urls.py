from django.urls import path
from .views import posts, post_detail

app_name = 'blog'
urlpatterns = [
    path('', posts, name="blog_home"),
    path('post_detail/<str:year>/<str:month>/<str:day>/<int:id>/<slug:slug>/', post_detail, name="post_detail"),
]
