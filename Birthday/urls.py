
from django.contrib import admin
from django.urls import path
from Employee.views import UpcomingBirthdayView, SendBirthdayEmailsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('upcoming-birthdays/', UpcomingBirthdayView.as_view(), name='upcoming-birthdays'),
    path('send-birthday-emails/', SendBirthdayEmailsView.as_view(), name='send-birthday-emails'),
]
