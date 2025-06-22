from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # renders form
    path('solve/', views.solve, name='solve'),    # handles solving
]
