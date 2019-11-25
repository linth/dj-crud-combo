"""dj_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf0
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import url
from cbv import views

app_name = 'cbv'

urlpatterns = [
    # using path.
    path('', views.BookList.as_view(), name='list'),
    path('add/', views.BookCreate.as_view(), name='add'),
    path('drafts/', views.DraftsBookList.as_view(), name='drafts'),
    path('update/<int:pk>', views.BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='delete'),
    path('detail/<int:pk>', views.BookDetail.as_view(), name='detail'),

    # using urrl
    # url(r'^$', views.BookList.as_view(), name='list'),
    # url(r'^add/$', views.BookCreate.as_view(), name='add'),
    # url(r'^drafts/$', views.DraftsBookList.as_view(), name='drafts'),
    # url(r'^update/(?P<pk>[0-9]+)$', views.BookUpdate.as_view(), name='update'),
    # url(r'^delete/(?P<pk>[0-9]+)$', views.BookDelete.as_view(), name='delete'),

    # API
    path('get_all_book/', views.get_all_book, name='get_all_book'),
    path('search_book_by_get_method', views.search_book_by_get_method, name='search_book_by_get_method'),
    path('search_book_by_post_method', views.search_book_by_get_method, name='search_book_by_post_method'),
]
