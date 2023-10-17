
from django.urls import path 
from . import views

urlpatterns = [
    path("" , views.index , name='home'),
    path('signup',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('addproducts/', views.add_products_view, name='addproducts'),
]
