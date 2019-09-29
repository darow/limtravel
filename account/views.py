from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.contrib import auth


def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    args = {'form': form}
    args.update(csrf(request))

    return render_to_response('account/register.html', args)


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/account/check')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('account/login.html', args)

    else:
        return render_to_response('account/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def check(request):
    data = {'username': auth.get_user(request).username}
    return render_to_response('account/check.html', data)
