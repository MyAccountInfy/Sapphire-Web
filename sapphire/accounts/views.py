from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def home(request):
    redirect('profile')

def profile(request):
    return render(request, "accounts/profile.html")

def signup(request):
    # Checks if the user is sending their data (POST) or getting the form (GET)
    if(request.method == 'POST'):
        form = SignupForm(request.POST)
        # Makes sure the user filled out the form correctly as dictated by forms.py
        if form.is_valid():
            user = form.save(commit=False)
            # Sets the user to deactive until they confirm email
            user.is_active = False
            # Saves the user to the server
            user.save()
            current_site = get_current_site(request)
            # Sends the user an email based on the email template and the info passed in here
            message = render_to_string('emails/activate_account.html', {
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your Sapphire account (named by Armaan Goel).'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'accounts/please_confirm.html')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})

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
        return render(request, 'accounts/account_confirmed.html')
    else:
        return HttpResponse('Activation link is invalid!')

def logoutLander(request):
    return render(request, 'accounts/logout_lander.html')