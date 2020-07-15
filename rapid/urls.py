from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path('about', views.about),
    path('blog', views.blog),
    path('blog_single', views.blog_single),
    path('hosting', views.hosting),
    path('contact', views.contact),
    path('domain', views.domain),
]