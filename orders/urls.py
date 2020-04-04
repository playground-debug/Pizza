from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('signup', views.signupuser, name="signupuser"),
    path('logout', views.logoutuser, name="logoutuser"),
    path('login', views.loginuser, name="loginuser"),
    path('menu', views.menu, name="menu"),
    path('customise0/<name>', views.customise0, name="customise0"),
    path('customise1/<name>', views.customise1, name="customise1"),
    path('customise2/<name>', views.customise2, name="customise2"),
    path('customise3/<str:name>', views.customise3, name="customise3"),
    path('cart', views.cart, name="cart"),
    path('discard/<int:order_id>', views.discard, name="discard"),
    path('placeorder', views.placeorder, name="placeorder"),
    path('order', views.order, name="order"),
    path('complete/<int:order_id>', views.complete, name="complete"),
]
