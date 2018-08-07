from django.conf import settings
from django.shortcuts import redirect


def index(request):
    page = settings.MAIN_PAGE if request.user.is_authenticated else 'login'
    return redirect(page)
