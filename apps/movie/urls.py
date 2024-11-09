
from django.urls import path, include

from apps.movie.views import Create,List,Update
 

urlpatterns = [

    path('create/', Create, name='create-movie'),
    path('list/', List, name='movies'),
    path('<int:id>/update/',Update, name='update-movie'),
]