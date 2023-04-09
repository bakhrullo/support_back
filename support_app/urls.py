from django.urls import path

from .views import *

urlpatterns = [
    path('agent', AgentView.as_view()),
    path('project', ProjectView.as_view())
]

