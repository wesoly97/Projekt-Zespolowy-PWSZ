from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_<int:user_id>/', views.usersHOME, name='usersHOME'),
    path('user<int:user_id>/p<int:post_id>/', views.post, name='post'),
    path('user<int:user_id>/pM<int:post_id>/', views.postM, name='postM'),

    path('forum_user_<int:user_id>/', views.user_at_forum, name='user_at_forum'),
    path('math_page2_user_<int:user_id>/', views.math_page2, name='math_page2'),
    path('math_page3_user_<int:user_id>/', views.math_page3, name='math_page3'),


    path('forum_user_<int:user_id>/p<int:post_id>/delete/', views.delete, name='delete'),
    path('forum_user_<int:user_id>/p<int:post_id>/delete_odp<int:answer_id>/', views.delete_odp, name='delete_odp'),
    path('forum_user_<int:user_id>/p<int:post_id>/odp/', views.odp, name='odp'),
    path('forum_user_<int:user_id>/p<int:post_id>/delete_odpM<int:answer_id>/', views.delete_odpM, name='delete_odpM'),
    path('forum_user_<int:user_id>/p<int:post_id>/odpM/', views.odpM, name='odpM'),
    path('forum_user_<int:user_id>/p<int:post_id>/check/', views.check, name='check'),
    path('forum_user_<int:user_id>/add/', views.add, name='add'),

    path('userScore_<int:user_id>', views.score, name='userScore'),

    path('history_<int:user_id>', views.history, name='history'),


    path('register2', views.register2, name='register2'),
    path('register1', views.register1, name='register1'),

    path('addQuestionOpen_user_<int:user_id>/', views.addQuestionView, name='addQuestionOpen'),
    path('addQuestionClose_user_<int:user_id>/', views.addQuestionViewClosedQuestion, name='addQuestionClose'),
    path('addQuestionOpenToDatabase/', views.addQuestionOpenToDatabase, name='addQuestionOpenToDatabase'),
    path('addQuestionCloseToDatabase/', views.addQuestionCloseToDatabase, name='addQuestionCloseToDatabase'),

    path('login', views.login, name='login'),
    path('log_in', views.login_user, name='log_in'),
    path('logout', views.logout, name='log_out'),
    path('userPanel_user_<int:user_id>/', views.userPanel, name='userPanel'), 
]