from django.contrib import auth
from django.shortcuts import render_to_response


def main_page(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/main_page.html', args)
