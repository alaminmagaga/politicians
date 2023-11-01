
from django.urls import path,include
from .views import  PresidentList, PresidentDetail
app_name = 'president'

urlpatterns = [
   
    path('', PresidentList.as_view(), name='president-list'),
    path('<int:pk>/', PresidentDetail.as_view(), name='detail'),
    
]
