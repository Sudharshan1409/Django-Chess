from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'home.html'

class UserProfile(TemplateView):
    template_name = 'userprofile.html'
