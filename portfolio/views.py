# -*- coding: utf-8 -*- 
from django.template.response import TemplateResponse
from portfolio.forms import ContactForm
from django.shortcuts import render
from django.core.mail.message import EmailMultiAlternatives


def index(request):
    return TemplateResponse(request, 'portfolio/index.html',{})

def about(request):
    return TemplateResponse(request, 'portfolio/about.html',{})

def offer(request):
    return TemplateResponse(request, 'portfolio/offer.html',{})

def contact(request):
    form = ContactForm(request.POST or None)
    success = None
    if request.method == "POST":
        if form.is_valid():
            text_content = u"Email: "+form.cleaned_data['email']+u". Wiadomość: "+form.cleaned_data['message']
            html_content = u"<b>Email:</b> "+form.cleaned_data['email']+u"<br /> <b>Wiadomość:</b> "+form.cleaned_data['message']
            msg = EmailMultiAlternatives(u'Kontakt przez portfolio od: '+unicode(form.cleaned_data['name']), text_content, form.cleaned_data['email'], ['przemyslawpiekarski@elodz.eu'])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            form = ContactForm()
            success = "Wiadomość została wysłana."
    return TemplateResponse(request, 'portfolio/contact.html',{'form':form, 'success':success})

#Errors
def error404(request):
    message = "Strony nie znaleziono – niestety strona o podanym adresie nie istnieje lub została usunięta!"
    return render(request, 'errors/error.html',{'message':message, 'error':'404'}, status=404)

def error500(request):
    message = "Wewnętrzny błąd serwera – serwer napotkał niespodziewane trudności, które uniemożliwiły zrealizowanie żądania!"
    return render(request, 'errors/error.html',{'message':message, 'error':'500'}, status=500)

def error403(request):
    message = "Dostęp zabroniony – konfiguracja bezpieczeństwa nie pozwala na wyświetlenie żądanego zasobu!"
    return render(request, 'errors/error.html',{'message':message, 'error':'403'}, status=403)

def error400(request):
    message = "Nieprawidłowe zapytanie – żądanie nie może być obsłużone przez serwer!"
    return render(request, 'errors/error.html',{'message':message, 'error':'400'}, status=400)
