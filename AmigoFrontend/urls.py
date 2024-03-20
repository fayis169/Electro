from django.urls import path
from AmigoFrontend import views

urlpatterns = [
    path('Home/', views.Home, name="Home"),
    path('home_product/', views.home_product, name="home_product"),
    path('single_product/<int:proid>/', views.single_product, name="single_product"),
    path('filter_product/<cat_name>/', views.filter_product, name="filter_product"),
    path('about_us/', views.about_us, name="about_us"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('save_contact/', views.save_contact, name="save_contact"),

    path('signup_login/', views.signup_login, name="signup_login"),
    path('save_signup/', views.save_signup, name="save_signup"),

    path('signin_login/', views.signin_login, name="signin_login"),
    path('userlogin/', views.userlogin, name="userlogin"),

    path('lorout/', views.lorout, name="lorout"),

    path('cart/', views.cart, name="cart"),
    path('savecart/', views.savecart, name="savecart"),
    path('cart_delete/<int:de>/', views.cart_delete, name="cart_delete"),

    path('checkout/', views.checkout, name="checkout"),
]