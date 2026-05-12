from django.urls import path
from . import views
from .views import (
    cake_list_api,
    cake_detail_api,
    category_list,
    branch_list,
    orders_api,
    cancel_order,
    order_detail_api,
)


urlpatterns = [
    path('cakes/', views.cake_list_api),
    path('cakes/<int:id>/', views.cake_detail_api),
    path("categories/", category_list),
    path("branches/", branch_list),
    path("orders/", orders_api),
    path("orders/<int:id>/", order_detail_api),
    path("orders/<int:pk>/cancel/", cancel_order),
]
