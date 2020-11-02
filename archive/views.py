# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect

# from .models import Archive


def index(request):
    template = loader.get_template("archive/index.html")
    discord_key = request.get("code")
    context = {
        "discord_key": discord_key,
    }
    return HttpResponse(template.render(context, request))


