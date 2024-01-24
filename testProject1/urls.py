
from django.contrib import admin
from django.urls import path

from human.views import human_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('human_list/', human_list, name='human_list')
]
