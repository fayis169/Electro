from django.urls import path
from AmigoApp import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('editcategory/<int:e>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:u>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:d>/', views.deletecategory, name="deletecategory"),

    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('editproduct/<int:e>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:u>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:d>/', views.deleteproduct, name="deleteproduct"),

    path('admin_login/', views.admin_login, name="admin_login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

    path('display_contact/', views.display_contact, name="display_contact"),
    path('delete_contact/<int:d>/', views.delete_contact, name="delete_contact"),
]
