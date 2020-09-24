from django.urls import path

from user import views

urlpatterns = [
    path('activity_periods/', views.UserActivityPeriodsView.as_view(), name='user_activity_periods'),
    ]
