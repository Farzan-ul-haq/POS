from django.urls import path, include

from . import views


app_name = 'core'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:pr_id>/update/', views.update, name='update'),
    path('<int:pr_id>/delete/', views.delete, name='delete'),
]
