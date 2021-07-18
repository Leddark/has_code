from django.urls import path
from . views import home , index , code , home2

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home , name="home"),
    path('has', home2 , name="home2"),
    path('index', index , name="index"),
    path('code', code , name="code"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
