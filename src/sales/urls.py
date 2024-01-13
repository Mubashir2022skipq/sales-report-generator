from django.urls import path
#from sales.models import Sale
from .views import (
    
    home_view,    
    SaleListView,
    SaleDetailView,
    
    )


app_name = 'sales'

urlpatterns = [
    path('',home_view,name='home'),
    path('sales/',SaleListView.as_view(),name='list'),
    path('sales/<pk>/',SaleDetailView.as_view(),name='detail')
    #path('sales/<int:pk>/', SaleDetailView.as_view(), name='detail'),
   
    


]
