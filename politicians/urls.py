# house_of_representatives_api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('president/', include(('presidents.urls', 'President'), namespace='president-api')),

]
