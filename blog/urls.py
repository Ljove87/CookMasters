from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostDetailView


urlpatterns = [
    path('', views.index_view, name='index-page'),
    path('blog/', views.blog_view, name='blog-page'),
    path('blog/<slug:slug>', views.PostDetailView.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
