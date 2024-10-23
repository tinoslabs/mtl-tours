"""
URL configuration for travel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from .views import category_selection

urlpatterns = [
    path('',views.index,name='index'),
    path('category/<int:category_id>/',views. package_view, name='package_view'),
    path('category-selection/', category_selection, name='category_selection'),
    path('reservation/',views.reservation,name='reservation'),
    path('get_packages/<int:category_id>/', views.get_packages, name='get_packages'),
    path('submit_booking/', views.submit_booking, name='submit_booking'),
    path('package_view', views.package_view, name='package_view'),
    path('gallery/<int:package_id>/', views.gallery_view, name='gallery_url'),


    
    path('user_login',views.user_login,name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('admin_booking_view',views.admin_booking_view,name='admin_booking_view'),
    path('admin_delete_bookings/<int:id>/',views.admin_delete_bookings,name='admin_delete_bookings'),
    path('admin_contact_view',views.admin_contact_view,name='admin_contact_view'),
    path('admin_delete_contact/<int:id>/',views.admin_delete_contact,name='admin_delete_contact'),

    path('admin_add_packages', views.admin_add_packages, name='admin_add_packages'),
    path('admin_packages_view',views.admin_packages_view,name='admin_packages_view'),
    path('admin_update_packages/<int:package_id>/',views.admin_update_packages,name='admin_update_packages'),
    path('admin_delete_packages/<int:id>/',views.admin_delete_packages,name='admin_delete_packages'),

    path('admin_add_categories', views.admin_add_categories, name='admin_add_categories'),
    path('admin_category_view',views.admin_category_view,name='admin_category_view'),
    path('admin_update_categories/<int:id>/',views.admin_update_categories,name='admin_update_categories'),
    path('admin_delete_categories/<int:id>/',views.admin_delete_categories,name='admin_delete_categories'),
    
]



    
