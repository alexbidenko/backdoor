from django.shortcuts import render
from django.http import HttpResponse
import socket


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def ideas(request, date_start, date_end):
    response = "You're looking at the results of question %s %s."
    return HttpResponse(response % (date_start, date_end))


def create(request):
    return render(request, 'repository/create.html')


def command(request):
    if request.method == 'POST':
        sock = socket.socket()
        sock.connect(('localhost', 9106))
        sock.sendall(str.encode(request.POST['command']))

        data = sock.recv(1024)
        sock.close()

        return HttpResponse(data)
    else:
        return render(request, 'repository/create.html')
