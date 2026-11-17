from django.urls import path

from . import views

urlpatterns = [

    path('projects/',views.ProjectListCreateView.as_view()),
    path('projects/<str:uuid>/',views.ProjectRetrieveUpdateDestroy.as_view()),
    path('assigned-projects/',views.AssignedProjectListCreateView.as_view()),
    path('assigned-projects/<str:uuid>/',views.AssignedProjectRetrieveUpdateDestroy.as_view()),
    path('tasks/',views.TaskListCreateView.as_view()),
    path('tasks/<str:uuid>/',views.TaskRetrieveUpdateDestroy.as_view()),
    path('create-task-ai/<str:uuid>/',views.TaskCreateWithAi.as_view()),


]
