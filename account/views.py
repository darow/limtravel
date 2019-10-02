from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, redirect, render
from django.template.context_processors import csrf
from django.contrib import auth
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, CustomUserAuthForm
from decorators.decorators import create_args_with_username
from .models import CustomUser



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


# class LoginView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('/')
#     template_name = 'account/login.html'
#

def became_partner(request):
    user = auth.get_user(request)
    host = request._current_scheme_host
    user.partner_link = host + '/invited_by/' + str(user.id)
    user.save()
    return redirect('/account/private_aria/')


@create_args_with_username
def private_area(request, args):
    partner_link = auth.get_user(request).partner_link
    args['partner_link'] = partner_link
    invited_users_list = CustomUser.objects.filter(invited_by=auth.get_user(request))
    args['invited_users'] = invited_users_list
    return render(
        request,
        'account/private_area.html',
        args,
    )


def register(request):
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.invited_by = CustomUser.objects.get(pk=request.COOKIES.get('invited_by'))
            form.save()
            response = redirect('/')
            response.delete_cookie('invited_by')
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return response
    else:
        form = CustomUserCreationForm()
    args = {'form': form}
    args.update(csrf(request))

    return render_to_response('account/signup.html', args)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('account/login.html', args)

    else:
        args['form'] = CustomUserAuthForm()
    return render_to_response('account/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")

