from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer
from .models import Reminder
# from rest_framework import viewsets

class ReminderCreateView(APIView):
    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        remainder = Reminder.objects.all()
        serializer = ReminderSerializer(remainder,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)






def reminder_form(request):
    return render(request, 'reminders/form.html')
