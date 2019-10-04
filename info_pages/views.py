from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from account.models import CustomUser
from decorators.decorators import create_args_with_username
from django.core.exceptions import ObjectDoesNotExist


def invited_by(request, user_id):
    args = {}
    cookie_saved_inviter = request.COOKIES.get('invited_by')
    if cookie_saved_inviter:
        username = CustomUser.objects.get(pk=cookie_saved_inviter).username
        args['msg'] = 'Вы приглашены пользователем {}. Зарегистрируйтесь, чтобы сохранить это.'.format(username)
        return render_to_response('main_page/links_in_header/main_page.html', args)
    else:
        try:
            user = CustomUser.objects.get(pk=user_id)
            response = redirect('/')
            response.set_cookie('invited_by', user_id, max_age=365 * 24 * 60 * 60)
        except ObjectDoesNotExist:
            args['msg'] = 'Пригласительная ссылка содержит неверный идентификатор пользователя'
            return render_to_response('main_page/links_in_header/main_page.html', args)
        return response


@create_args_with_username
def main_page(request, args):
    cookie_saved_inviter = request.COOKIES.get('invited_by')
    if cookie_saved_inviter:
        username = CustomUser.objects.get(pk=cookie_saved_inviter).username
        args['msg'] = 'Вы приглашены пользователем {}. Зарегистрируйтесь, чтобы сохранить это.'.format(username)
    return render_to_response('main_page/links_in_header/main_page.html', args)


@create_args_with_username
def tourist_visas(request, args):
    return render_to_response('main_page/links_in_header/tourist_visas.html', args)


@create_args_with_username
def long_term_visas(request, args):
    return render_to_response('main_page/links_in_header/long_term_visas.html', args)


@create_args_with_username
def international_passport(request, args):
    args = {'username': auth.get_user(request).username}
    return render_to_response('main_page/links_in_header/international_passport.html', args)


@create_args_with_username
def invitations(request, args):
    return render_to_response('main_page/links_in_header/invitations.html', args)


@create_args_with_username
def about_us(request, args):
    return render_to_response('main_page/links_in_footer/about_us.html', args)


@create_args_with_username
def payment(request, args):
    return render_to_response('main_page/links_in_footer/payment.html', args)


@create_args_with_username
def contacts(request, args):
    return render_to_response('main_page/links_in_footer/contacts.html', args)
