from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('delete_owner_add_room', views.delete_owner_add_room, name='delete_owner_add_room'),
    path('owner_view_room',views.owner_view_room,name='owner_view_room'),
    path('add_room_cat',views.add_room_cat,name='add_room_cat'),
    path('add_room_subcat',views.add_room_subcat,name='add_room_subcat'),
    path('cat',views.cat,name='cat'),
    path('subcat',views.subcat,name='subcat'),
    path('user_check_email',views.user_check_email,name='user_check_email'),
    #path('user_check_pass', views.user_check_pass, name='user_check_pass'),
    path('view_room_owner', views.view_room_owner, name='view_room_owner'),
    path('view_booking_owner',views.view_booking_owner, name='view_booking_owner'),
    path('owner_login', views.owner_login, name='owner_login'),
    path('owner_add_room', views.owner_add_room, name='owner_add_room'),
    path('ownerrecords', views.ownerrecords, name='ownerrecords'),
    #path('owner_upload_image', views.owner_upload_image, name='owner_upload_image'),
    path('viewusersrecords', views.viewusersrecords, name='viewusersrecords'),
    path('ownerD', views.ownerD, name='ownerD'),
    path('owner_check_email',views.owner_check_email,name='owner_check_email'),
    path('al', views.al, name='al'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('admin_logout',views.admin_logout, name='admin_logout'),
    path('contact', views.contact, name='contact'),
    path('owner', views.owner, name='owner'),
    path('aboutus', views.about, name='about'),
    path('home', views.home, name='home'),
    path('test', views.test, name='test'),
    path('search_property', views.search_property, name='search_property'),
    path('sf', views.signup, name='signup'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('owner_logout',views.owner_logout, name='owner_logout'),
    path('lf', views.login, name='login'),
    path('user_dash_board_view', views.user_dash_board_view, name='user_dash_board_view'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    path('', views.index, name='index'),

]

