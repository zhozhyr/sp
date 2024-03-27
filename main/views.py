from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic import TemplateView
# def home(request):
#     return render(request, "index.html")

class HomePageView(TemplateView):
    template_name = 'home.html'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address'],
                'phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("main:home")

    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})