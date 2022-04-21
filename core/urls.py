from django.urls import path
from django.contrib.auth import views as auth_view

from core.views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),


    path('reset-password/', auth_view.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    path('reset-password-done/', auth_view.PasswordResetDoneView.as_view(), name=''),
    path('reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-complete/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

"""
from django.contrib.auth import views as auth_view
1 - Submit email form                       // PasswordResetView.as_view()
2 Email sent success message                // PasswordResetDoneView.as_view()
3 - Link to password Rest form in email     // PasswordResetConfirmView.as_view()
4 - Password successfully changed message   // PasswordResetCompleteView.as_view()
"""