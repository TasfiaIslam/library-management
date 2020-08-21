from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('book/', views.displayBooks, name="book"),

    path('create_book/', views.createBook, name="create_book"),
    path('update_book/<str:pk>/', views.updateBook, name="update_book"),
    path('delete_book/<str:pk>/', views.deleteBook, name="delete_book"),

    path('order_book/<str:pk>/', views.orderBook, name="order_book"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),

    path('rent_book/<str:pk>/', views.rentBook, name="rent_book"),

    path('member/<str:pk>/', views.member, name="member"),
    path('create_member/', views.createMember, name="create_member"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('user_page/', views.userPage, name="user_page"),
    path('account/', views.accountSettings, name="account"),

    path('upload_pdf/', views.uploadPdf, name="upload_pdf"),
    path('display_pdf/', views.displayPdf, name="display_pdf"),
    
]