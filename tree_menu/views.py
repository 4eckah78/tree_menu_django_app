from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request, 'contacts.html')

def web_development(request):
    return render(request, 'web_development.html')

def seo(request):
    return render(request, 'seo.html')

def design(request):
    return render(request, 'design.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')
