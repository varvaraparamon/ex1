from django.urls import path, include
from . import views
from . import api_views

app_name = 'orders'

urlpatterns = [
    path('list/', views.order_list, name='order_list'),
    path('api/orders/', api_views.OrderListCreateAPIView.as_view(), name='api_orders'),
    path('api/orders/<int:pk>/', api_views.OrderRetrieveUpdateDestroyAPIView.as_view(), name='api_order_detail'),
]