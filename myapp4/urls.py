from .views import index
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('add-post', , name='add-post'),
]