from django.urls import path, include

from . import views

app_name = "blog"

urlpatterns =[
    path('blog/', views.blog, name = 'blog'),
    path('', views.personalblog, name = 'personalblog'),
    path('blog/<slug>/', views.blogDetails, name = 'blogDetails'),
    path('search/', views.search_blog, name = 'search_blog')
]