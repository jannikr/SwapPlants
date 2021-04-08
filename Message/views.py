from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader

from Message.models import DirectMessage
from django.contrib.auth.models import User

''' Messages View '''


@login_required()
def messages(request):
    context = {}
    user = request.user
    messages = DirectMessage.get_message(user=user)
    active_message = None
    directs = None

    if messages:
        message = messages[0]
        active_message = message['user'].username
        directs = DirectMessage.objects.filter(user=user, receiver=message['user'])
        directs.update(isOpened=True)

        context = {
            'directs': directs,
            'messages': messages,
            'active_message': active_message,
        }

    template = loader.get_template('messages.html')
    return HttpResponse(template.render(context, request))


@login_required()
def directs(request, username):
    user = request.user
    messages = DirectMessage.get_message(user=user)
    active_direct = username
    directs = DirectMessage.objects.filter(user=user, receiver__username=username)
    directs.update(isOpened=True)

    context = {
        'directs': directs,
        'messages': messages,
        'active_message': active_direct
    }

    template = loader.get_template('messages.html')

    return HttpResponse(template.render(context, request))


@login_required()
def send_direct(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')
    print(from_user)
    print(to_user_username)
    print(body)

    if request.method == 'POST':
        to_user = User.objects.get(username=to_user_username)
        DirectMessage.send_message(from_user, to_user, body)
        return redirect('messages')
    else:
        HttpResponseBadRequest()
