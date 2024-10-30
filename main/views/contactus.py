from django.shortcuts import render, redirect
from main.models.contactus import ContactUs



def contactus(request):
    return render(request, 'main/contactus/base.html')

def sendmessage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        project = request.POST.get('project')
        message = request.POST.get('message')

        ContactUs.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            project =project,
            message=message,
        )

        return redirect('contactus')

    return render(request, 'main/contactus/base.html')

