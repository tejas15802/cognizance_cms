from django.urls import path, include
from . import views
from adminapp.views import dashboard
from membersapp.views import dashboard as mDashboard
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home),
    path('login/', views.loginApp, name='login'),
    path('achievements/',views.achievements, name='achievements'),
    path('gallery/',views.gallery, name='gallery'),
    path('about/',views.contact_us, name='contact_us'),
    path('adminapp/', dashboard, name='adminapp'),
    path('applications/',views.applications, name='applications'),
    path('membersapp/', mDashboard, name='membersapp'),
    path('logout/', views.logoutApp, name='logout'),
    path('apply/',views.apply, name='apply'),
    path('<str:member_name>/',views.member),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="pages/password_reset.html"), name="rest_password"),   
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),   
    path('reset_password/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),   
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),   
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += static(settings.FILE_URL, document_root= settings.FILE_ROOT)
