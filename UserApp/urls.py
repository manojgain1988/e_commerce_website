from django.urls import path, include
from UserApp.views import user_logout
urlpatterns = [
    path('logout/', user_logout,name='user_logout'),
  
   
]
