from django.shortcuts import render
from django.http import HttpResponse
from .models import Pin


def index(request):
    context = {'pins_on_board', Pin.objects.all()}
    return render(request, 'main.html', {"context": context})


'''def get_pin_by_id(request, id):
    try:
        pin = Pin.objects.get(id)
    except:
        return HttpResponse(f"No such pin with id #{id}")
    return HttpResponse(f"Pin with id {id}: <br> {pin.desctription}")
'''