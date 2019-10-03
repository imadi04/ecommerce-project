from django.conf.urls import url
from cart import views
from django.urls import path
from django.contrib.auth import views as auth_views


app_name='cart'

urlpatterns=[
   path('register/',views.register,name='register'),
   path('',views.IndexView.as_view(),name='index'),
   path('user_login',views.user_login,name='user_login'),
   path('user_logout',views.user_logout,name='user_logout'),
   path('products/',views.products,name='products'),
   path('tracker/',views.tracker,name="tracker"),
   path('cart/',views.cart,name='cart'),
]
