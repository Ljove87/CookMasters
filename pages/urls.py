from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('o-nama/', views.about_view, name='about-page'),
    path('contact/', views.contact_view, name='contact-page'),
    path('recepti/', views.recipes_view, name='recipes-page'),
    path('obuka_ljudi/', views.training, name='obuka-page'),
    path('popup_kuvari/', views.popup_view, name='popup-page'),
    path('postavka_kuhinje/', views.meni, name='kuhinja-page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
