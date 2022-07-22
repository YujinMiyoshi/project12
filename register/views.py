from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from .forms import LoginForm, UserCreateForm
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import render_to_string

User = get_user_model()

class Login(LoginView):
    form_class = LoginForm
    template_name = 'register/login.html'

class Logout(LogoutView):
    template_name = 'register/login.html'

class UserCreate(CreateView):
    template_name = 'register/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('register/mail_template/create/aubject.txt', context)
        message = render_to_string('register/mail_template/create/message.txt', context)

        user.email_user(subject, message)
        return redirect('register:user_create_done')

class UserCreateDone(TemplateView):
    template_name = 'register/user_create_done.html'



# Create your views here.
