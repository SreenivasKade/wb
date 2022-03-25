from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MoveSerializer
from .models import Move
import time

# Create your views here.

######################   CONTROL VIEWS   #############################

def ControlView(request):    
    return render(request, 'ControlsApp/control.html')


def UpView(request):
    m = Move.objects.latest('pk')
    m.movement = 'up'
    m.time = time.time()
    m.save()
    print('UP')
    return redirect('ControlsApp:control')

def DownView(request):
    m = Move.objects.latest('pk')
    m.movement = 'down'
    m.time = time.time()
    m.save()
    print('DOWN')
    return redirect('ControlsApp:control')
    


def LeftView(request):
    m = Move.objects.latest('pk')
    m.movement = 'left'
    m.time = time.time()
    m.save()
    print('LEFT')
    return redirect('ControlsApp:control')



def RightView(request):
    m = Move.objects.latest('pk')
    m.movement = 'right'
    m.time = time.time()
    m.save()
    print("Right")
    return redirect('ControlsApp:control')
    


def StopView(request):
    m = Move.objects.latest('pk')
    m.movement = 'stop'
    m.time = time.time()
    m.save()
    print('STOP')
    return redirect('ControlsApp:control')
    


################   API VIEWS   #######################

@api_view(['GET'])
def APIControlView(request):
    data = Move.objects.latest('pk')
    serializer = MoveSerializer(data, many = False)

    return Response(serializer.data)