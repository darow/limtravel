from django.contrib import auth
from django.shortcuts import render_to_response


def main_page(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/links_in_header/main_page.html', args)


def tourist_visas(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/links_in_header/tourist_visas.html', args)


def long_term_visas(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/links_in_header/long_term_visas.html', args)


def international_passport(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/links_in_header/international_passport.html', args)


def invitations(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/links_in_header/invitations.html', args)


def about_us(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/links_in_footer/about_us.html', args)


def payment(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/links_in_footer/payment.html', args)


def contacts(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/links_in_footer/contacts.html', args)
