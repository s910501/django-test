from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
from .forms import NameForm
from .models import AuthorForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['464421145@qq.com',sender]
            if cc_myself:
                recipients.append(sender)
            send_mail(subject=subject, message=message, from_email=None,recipient_list=recipients)
            #send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/web/')
        else:
            return HttpResponse(form)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        form1 = AuthorForm()

    return render(request, 'name.html', {'form': form,'form1': form1})
