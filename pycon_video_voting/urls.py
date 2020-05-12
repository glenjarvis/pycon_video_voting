"""PyCon Video Voting Site URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vote.urls')),
    path('open_spaces/', include('open_spaces.urls')),
]
