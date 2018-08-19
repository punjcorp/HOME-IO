from django.shortcuts import render
from .models import IOSwitch

# Create your views here.


def index(request):
    io_switch_list = IOSwitch.objects.all()
    context = {'io_switch_list': io_switch_list}
    return render(request, 'HOME_IO_UI/home.html', context)


def likePost(request):
    if request.method == 'POST':
        posted_switch = request.POST['postedSwitch']
        ioSwitch = IOSwitch.obejcts.get(
            outlet_id=posted_switch.switchId)  # getting the liked posts
        ioSwitch.state = True
        ioSwitch.save()
        return HttpResponse("Success!")  # Sending an success response
    else:
        return HttpResponse("Request method is not a GET")
