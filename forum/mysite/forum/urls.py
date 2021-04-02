from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_<int:user_id>/', views.usersHOME, name='usersHOME'),
    path('user<int:user_id>/p<int:post_id>/', views.post, name='post'),

    path('forum_user_<int:user_id>/', views.user_at_forum, name='user_at_forum'),
    path('math_page_user_<int:user_id>/', views.math_page, name='math_page'),
    path('math_page2_user_<int:user_id>/', views.math_page2, name='math_page2'),
    path('math_page3_user_<int:user_id>/', views.math_page3, name='math_page3'),


    path('forum_user_<int:user_id>/p<int:post_id>/delete/', views.delete, name='delete'),
    path('forum_user_<int:user_id>/p<int:post_id>/delete_odp<int:answer_id>/', views.delete_odp, name='delete_odp'),
    path('forum_user_<int:user_id>/p<int:post_id>/odp/', views.odp, name='odp'),
    path('forum_user_<int:user_id>/add/', views.add, name='add'),

    path('register2', views.register2, name='register2'),
    path('register1', views.register1, name='register1'),

    path('addQuestion', views.addQuestionView, name='addQuestion'),
]