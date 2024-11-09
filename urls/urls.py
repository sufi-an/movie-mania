from django.urls import path, include
from apps.user.views import Index
# Put here all apps url
urlpatterns = [
    path("", Index, name='index'),
    path("user/", include("apps.user.urls")),
    path("movie/", include("apps.movie.urls")),
]
