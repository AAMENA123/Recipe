from django.urls import path, include
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', recipes),
    path('recipe/', recipes),
    path('home/',home),
    path('delete/<id>/', delete_recipe),
    path('update/<id>/', update_recipe),
    path('update/', update_recipe1),
    path('login/', login),
    path('register/', register),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
        
urlpatterns += staticfiles_urlpatterns()