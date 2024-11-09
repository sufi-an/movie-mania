
from django.urls import path, include

from apps.user.views import Login,Register,Logout
 

urlpatterns = [
    # path("profile/", profile, name="user-profile"),
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', Logout, name ='logout'),
]