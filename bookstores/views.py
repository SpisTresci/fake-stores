from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.files.base import ContentFile

# Create your views here.
from bookstores.models import Store


def example(request, name):
    string = Store.objects.get(name=name).file
    file_to_send = ContentFile(string)
    response = HttpResponse(file_to_send, 'application/x-gzip')
    response['Content-Length'] = file_to_send.size
    response['Content-Type'] = 'text/xml'
    return response