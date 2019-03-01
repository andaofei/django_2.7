from django.shortcuts import render
import MySQLdb

# from .models import UserMessage
# Create your views here.
def getform(request):
    # all_message = UserMessage.objects.all()
    # from message in all_message:
    return render(request, 'message_form.html');