
from django.urls import path, include

from apps.movie.views import MovieListView,MovieCreateView,MovieUpdateView,MovieDeleteView,MovieDetailView
 

urlpatterns = [

    path('create/', MovieCreateView.as_view(), name='create-movie'),
    path('list/', MovieListView.as_view(), name='movies'),
    path('<int:pk>/detail/',MovieDetailView.as_view(), name='detail-movie'),
    path('<int:pk>/update/',MovieUpdateView.as_view(), name='update-movie'),
    path('<int:pk>/delete/',MovieDeleteView.as_view(), name='delete-movie'),
]