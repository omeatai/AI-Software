from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order', views.order, name='order'),
    path('orders', views.orders, name='orders'),
    path('order/<int:pk>', views.edit_order, name='edit-order'),
]