from django.urls import path
from . import views

urlpatterns = [
    path('submit_obituary/', views.submit_obituary, name='submit_obituary'),
    path('view_obituaries/', views.view_obituaries, name='view_obituaries'),
]
# project/urls.py (or whatever your project name is, e.g., myproject/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('obituaries.urls')),
]
