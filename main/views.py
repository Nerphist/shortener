import json

from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.core.validators import URLValidator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_GET, require_POST

from main import repository


@require_GET
def index(request):
    return render(request, 'index.html')


@require_POST
def shorten(request: WSGIRequest):
    url = request.POST['url']

    try:
        URLValidator()(url)
    except ValidationError:
        return HttpResponse(status=400)

    url_model, created = repository.get_or_create_url(url)

    return HttpResponse(content=json.dumps({
        'url': f'{request.build_absolute_uri("/")}redirect/{url_model.id}',
        'created': created,
        'clicks': url_model.clicks_count,
    }).encode())


@require_GET
def redirect_to_url(request: HttpRequest, url_id: int):
    url_model = repository.get_url_by_id(url_id)
    if not url_model:
        return redirect('/')
    else:
        repository.increment_clicks(url_model)
        return redirect(url_model.url)
