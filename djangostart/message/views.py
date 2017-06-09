from django.shortcuts import render
from .models import UserMessage

# Create your views here.
def form(request):
    all_messages = UserMessage.objects.all()
    user_message = UserMessage()
    user_message.name = "bobby1"
    user_message.address = "上海"
    user_message.email = "ddd@qq.com"
    user_message.message = "helloworld1"
    user_message.save()
    return render(request,'form1.html')
