from django.shortcuts import render, redirect
from django.http import BadHeaderError
from django.core.mail import send_mail
from django.views.generic import TemplateView


from django.conf import settings


from django.contrib import messages
from .forms import ContactForm
# Create your views here.



class HomePageView(TemplateView):
    template_name = 'home.html'



def HomePage(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data.get('subject', f'New Message from {name}')
            from_email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            send_mail('Message Received', f'Dear {name}! I have received your message and will get back to you shortly. \n Thanks for contacting me.',\
                'settings.EMAIL_HOST_USER', [from_email] )
            #messages.info(request, 'Congratulations')
            return redirect('success')
        messages.warning(request, 'Please Go Back To The Form And Correct Your Error...')
    return render(request, 'home.html', {'form': form})

def successView(request):
    messages.success(request, 'Your message was sent successfully. I\'ll get back to you shortly...')
    return redirect('home')

def SkillsPage(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data.get('subject', f'New Message from {name}')
            from_email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            send_mail('Message Received', f'Dear {name}! I have received your message and will get back to you shortly. \n Thanks for contacting me.',\
                'settings.EMAIL_HOST_USER', [from_email] )
            return redirect('success')
        messages.warning(request, 'Please Go Back To The Form And Correct Your Error...')
    return render(request, 'skills.html', {'form': form})


def WorksPage(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data.get('subject', f'New Message from {name}')
            from_email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            send_mail('Message Received', f'Dear {name}! I have received your message and will get back to you shortly. \n Thanks for contacting me.',\
                'settings.EMAIL_HOST_USER', [from_email] )
            #messages.info(request, 'Congratulations')
            return redirect('success')
        messages.warning(request, 'Please Go Back To The Form And Correct Your Error...')
    return render(request, 'work.html', {'form': form})


def ResumePage(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data.get('subject', f'New Message from {name}')
            from_email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            send_mail('Message Received', f'Dear {name}! I have received your message and will get back to you shortly.\n Thanks for contacting me.',\
                'settings.EMAIL_HOST_USER', [from_email] )
            return redirect('success')
        messages.warning(request, 'Please Go Back To The Form And Correct Your Error...')
    return render(request, 'resume.html', {'form': form})


def bar_chart_view(request):
    y = [90,90,80,75,20,40,90,65]
    x = ['DS', 'DJ', 'CSS', 'HT', 'BS', 'JS', 'RF', 'AD']
    plt.bar(y)
    bar = plt.show()
    plt.savefig('bar')
    return render(request, 'skills.html', {'bar': bar})

