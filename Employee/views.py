from rest_framework import generics, status
from .models import Employee
from .serializer import EmployeeSerializer
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.response import Response


class UpcomingBirthdayView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        today = datetime.now().date()
        one_week_later = today + timedelta(days=7)
        return Employee.objects.filter(birthday__range=[today, one_week_later])


class SendBirthdayEmailsView(generics.GenericAPIView):
    def get(self, request):
        today = datetime.now().date()
        one_week_later = today + timedelta(days=7)
        employees = Employee.objects.filter(birthday__range=[today, one_week_later])

        if not employees:
            return Response({"message": "No upcoming birthdays to celebrate"}, status=status.HTTP_200_OK)

        for employee in employees:
            email_subject = "Happy Birthday!"
            email_template = "email_templates/birthday_email.html"
            email_context = {
                "employee_name": employee.first_name,
                # Other context variables
            }
            #email_message = render_to_string(email_template, email_context)
            email_message = "Happy Birthday"
            send_mail(email_subject, email_message, "sender@example.com", [employee.email])

        return Response({"message": "Birthday emails sent"}, status=status.HTTP_200_OK)

