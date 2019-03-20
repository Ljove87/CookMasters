from django.shortcuts import render, redirect

from django.contrib import messages
from . models import Post
from django.core.mail import send_mail
from django.views.generic import DeleteView, ListView


def index_view(request):
    return render(request, 'blog/index_view.html')

def blog_view(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog_view.html', context)

class PostDetailView(DeleteView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
