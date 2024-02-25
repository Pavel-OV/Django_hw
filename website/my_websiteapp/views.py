from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Cтраница index загрузилась")
    return HttpResponse("<h1>Привет! Вы на моей страничке.</h1>")

def about(request):
    logger.info("Cтраница about загрузилась")
    return HttpResponse("<h1>Страница обо мне</h1")