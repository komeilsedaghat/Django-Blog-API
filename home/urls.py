from django.urls import path,re_path
from . import views


app_name = 'home'




urlpatterns = [

    path('articles/',views.ListArticleView.as_view(),name='home'),
    path('articles/detail/<slug:slug>/',views.DetailArticleView.as_view(),name='detail'),
    path('articles/delete/<slug:slug>/',views.DeleteArticleView.as_view(),name='delete'),
    path('articles/add-article/',views.AddArticleView.as_view(),name='add-article'),
    path('articles/update/<slug:slug>/',views.UpdateArticleView.as_view(),name='update'),
]


