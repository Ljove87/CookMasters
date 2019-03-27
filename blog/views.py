from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from . models import Post
from django.core.mail import send_mail
from django.views.generic import DetailView, ListView


def index_view(request):
    return render(request, 'blog/index_view.html')

def blog_view(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog_view.html', {'posts': posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
