from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from . import auth_views
from .views import (
    cake_list_api,
    cake_detail_api,
    category_list,
    branch_list,
    orders_api,
    my_orders,
    cancel_order,
    order_detail_api,
    ai_chat,
)

urlpatterns = [
    # AI
    path("ai/chat/", ai_chat),

    # Cakes
    path("cakes/", cake_list_api),
    path("cakes/<int:id>/", cake_detail_api),

    # Categories
    path("categories/", category_list),

    # Branches
    path("branches/", branch_list),

    # Orders
    path("orders/", orders_api),
    path("my-orders/", my_orders),
    path("orders/<int:id>/", order_detail_api),
    path("orders/<int:pk>/cancel/", cancel_order),
    path("register/", auth_views.register),
    path("login/", auth_views.login_user),
    path("profile/", auth_views.profile),
    path("token/refresh/", TokenRefreshView.as_view()),
]
