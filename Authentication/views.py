from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView, TemplateView
from Authentication.forms import RegistrationForm
from Authentication.tokens import account_activation_token
from Core.tasks import send_verification_email


class RegisterFormView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        message = create_message(self.request, user)
        mail_subject = 'Активация аккаунта в интернет-магазине'
        to_email = form.cleaned_data.get('email')
        send_verification_email.delay(to_email, message, mail_subject)
        return redirect('info_send_email')


class InfoAfterSendEmail(TemplateView):
    template_name = 'info_send_email.html'

    def get_context_data(self, **kwargs):
        context = super(InfoAfterSendEmail, self).get_context_data(**kwargs)
        context['message'] = 'На почту было выслано письмо с' \
                             ' подтверждением Вашей учетной записи.' \
                             ' Пожалуйста, проверьте вашу почту!'
        return context


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Activation link is invalid!')


def create_message(request, user):
    current_site = get_current_site(request)
    message = render_to_string('acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token': account_activation_token.make_token(user),
    })

    return message
