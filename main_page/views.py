from django.contrib import auth
from django.shortcuts import render_to_response


def main_page(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/main_page.html', args)


def tourist_visas(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/tourist_visas.html', args)

def long_term_visas(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/long_term_visas.html', args)

def international_passport(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/international_passport.html', args)

def invitations(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/invitations.html', args)
