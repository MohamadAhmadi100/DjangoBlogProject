from django.shortcuts import render, get_object_or_404
from .models import Post


def posts(request):
    all_posts = Post.public_manager.all()
    return render(request, 'blog/all_posts.html', {'all_posts': all_posts})


def post_detail(request, id, *args, **kwargs):
    post = get_object_or_404(Post, id=id, status='public')
    return render(request, 'blog/post_detail.html', {'post': post})
