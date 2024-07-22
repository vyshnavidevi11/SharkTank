"""ssp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from userapp import views as userapp_views
from adminapp import views as adminapp_views
from mainapp import views as mainapp_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #userapp
    path('dashboard',userapp_views.user_dashboard,name="dashboard"),
    path('predict',userapp_views.prediction,name="prediction"),
    path('user_profile',userapp_views.user_profile,name="user_profile"),
    path('user_login',userapp_views.user_login,name="user_login"),
    #adminapp
    path('admin_login',adminapp_views.admin_login,name="admin_login"),
    path('index',adminapp_views.index,name="index"),
    path('pending_users',adminapp_views.pending_users,name="pending_users"),
    path('all_users',adminapp_views.all_users,name="all_users"),
    path('upload_dataset',adminapp_views.upload_dataset,name="upload_dataset"),
    path('view_dataset',adminapp_views.view_dataset,name="view_dataset"),
    path('algorithm1',adminapp_views.gradient_boosting_classifier,name="algorithm1"),
    path('algorithm2',adminapp_views.ada_boost_classifier,name="algorithm2"),
    path('algorithm3',adminapp_views.random_forest_classifier,name="algorithm3"),
    path('gbc-runalgo/<int:id>/',adminapp_views.gbc_runalgo,name="gbc_runalgo"),
    path('ada-runalgo/<int:id>/',adminapp_views.ada_runalgo,name="ada_runalgo"),
    path('rfc-runalgo/<int:id>/',adminapp_views.rfc_runalgo,name="rfc_runalgo"),
    path('analasis',adminapp_views.graph_analasis,name="analasis"),

    #mainapp
    path('',mainapp_views.home,name="home"),
    path('prediction/<int:id>/',mainapp_views.prediction_results,name="prediction_results"),
    path('contact',mainapp_views.contact,name="contact"),
    path('user_register',mainapp_views.user_register,name="user_register"),
    path('user_logout',userapp_views.user_logout,name="user_logout"),
    #Button functions urls
    path('user_accept/<int:id>',adminapp_views.accept,name="accept"),
    path('user_reject/<int:id>',adminapp_views.reject,name="reject"),
    path('user_change_status<int:id>',adminapp_views.change_status,name="change_status"),
    path('remove_status/<int:id>',adminapp_views.remove,name="remove"),
    path('admin_logout',adminapp_views.admin_logout,name="admin_logout"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
