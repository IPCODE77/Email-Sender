from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib import messages
import time

# Create your views here.
def sendemail(request):
    if request.method == 'POST':
        tomail= request.POST.get('tomail')
        content = request.POST.get('content')
        subject = request.POST.get('Subject')
        
        send_mail(subject,
                  content,
                settings.EMAIL_HOST,
                [tomail]  
                  )
        
        return render(
                request, 'html/email.html',
            )
    # else:
    #     return render(
    #         request, 'html/email.html',{'tittle':'send an mail'}
    #     )
    # context = {'tittle':tomail}
    return render(request,'html/email.html')