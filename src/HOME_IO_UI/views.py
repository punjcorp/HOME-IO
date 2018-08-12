from django.shortcuts import render
from .models import IOSwitch

# Create your views here.


def index(request):
    io_switch_list = IOSwitch.objects.all()
    context = {'io_switch_list': io_switch_list}
    return render(request, 'HOME_IO_UI/home.html', context)
