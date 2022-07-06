from django.shortcuts import render
from app.models import About, Project, Contact
from django.contrib import messages


def index(request):
    about = About.objects.all()
    projects = Project.objects.all()

    success = False

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # sweetalert kullanmayı deneyecem


        if Contact.objects.filter(email=email).exists():
            messages.error(request, 'Mesajınızı kısa bir süre önce aldık. En kısa sürede e-posta adresinize dönüş yapılacaktır.')
        else:
            success = True
            Contact.objects.create(name=name, email=email, message=message) 
            messages.success(request, 'Mesajınız başarıyla alındı.')



    return render(request, 'index.html', {
        'about': about,
        'projects': projects,
        'success': success
    })