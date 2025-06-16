from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_home, name='board_home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('add_project/', views.add_project, name='add_project'),
    path('add_programmer/', views.add_programmer, name='add_programmer'),
    path('add_task/', views.add_task, name='add_task'),

    path('mark_task_done/<int:task_id>/', views.mark_task_done, name='mark_task_done'),
    path('change_task_status/<int:task_id>/', views.change_task_status, name='change_task_status'),
    path('add/', views.add_item, name='add_item'),  # <-- здесь важно name='add_item'
    path('', views.home, name='home'),
]
handler404 = 'board.views.page_not_found_view'  # если есть, проверить существование функции
handler500 = 'board.views.server_error_view'   # если есть, проверить существование функции

