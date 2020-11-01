from django.shortcuts import render
from django.http import HttpResponse
import os
import awake

# Create your views here.
def wol(request):
    for x in range(5): awake.wol.send_magic_packet('B4:2E:99:A5:5F:07')
    return HttpResponse('Computer awoken!')