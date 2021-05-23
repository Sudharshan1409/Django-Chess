from django.views.generic import TemplateView, CreateView
from django.utils.decorators import method_decorator
from .decorators import should_not_be_logged_in
from django.contrib.auth.models import User
from .forms import UserForm
from django.shortcuts import reverse

class HomePage(TemplateView):
    template_name = 'home.html'

class UserProfile(TemplateView):
    template_name = 'userprofile.html'

@method_decorator(should_not_be_logged_in,name = 'dispatch')
class RegisterUserPage(CreateView):
    template_name = 'registration/user_form.html'
    context_object_name = 'form'
    model = User
    form_class = UserForm

    def get_success_url(self):
        return reverse('login')
