from django.urls import path
from thrifteg import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('test/', views.test, name='test'),  
    path('signup/', views.signup, name='signup'),  
    path('login/', views.login_view, name='login'),  # Updated to match views.py
    path('mainpage/', views.mainpage, name='mainpage'),  
    path('wishlist/', views.view_wishlist, name='wishlist'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_from_wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
