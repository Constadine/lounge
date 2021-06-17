from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('blog/', views.blog, name='blog'),
    path('bob_profile/<str:pk>/', views.bob, name='bob_profile'),
]
