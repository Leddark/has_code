from django.urls import path
from . views import home , index , code , home2


urlpatterns = [
    path('', home , name="home"),
    path('has', home2 , name="home2"),
    path('index', index , name="index"),
    path('code', code , name="code"),

]