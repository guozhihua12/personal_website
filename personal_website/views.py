# coding=utf-8
# from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from global_utils.my_email import send_mail

__author__ = 'apple'


def send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        name = request.POST.get('name')
        subject = '%s(email: %s) Leave a message in www.guozhihua.cc' % (name, email)
        send_mail(email, subject, comments)
        return render_to_response('index.html', {'location': 'email'}, context_instance=RequestContext(request))