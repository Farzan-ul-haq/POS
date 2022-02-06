from django.urls import path, include

from . import views

app_name = 'order'

urlpatterns = [
    path('<int:pr_id>/product/add/', views.add, name='add'),
    path('empty/', views.empty, name='empty'),
    path('submit/', views.submit, name='submit'),
    path('list/', views.list, name='list'),
]
