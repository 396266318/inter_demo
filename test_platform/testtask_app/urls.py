# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  15:33
@author: xuanyue
@file: urls.py
"""
from django.urls import path
from testtask_app import views


urlpatterns = [
    # 任务管理
    path('', views.testtask_manage),
    path('add_task/', views.add_task),
    path('edit_task/<int:tid>/', views.edit_task),
    path('delete_task/<int:tid>/', views.delete_task),
    path('result/<int:tid>/', views.result),
    path('save_task/', views.save_task),

    # 接口
    path('get_case_tree/', views.get_case_tree),
    path("run_task/", views.run_task),
]