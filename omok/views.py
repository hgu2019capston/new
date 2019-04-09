from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import OmokSerializer
from .models import Stone

def GameView(request):
    template = 'omok/dynamicpage.html'
    Stone_data = Stone.objects.all()
    return render(request, template, {
        'Stone_data' : Stone_data,
    }) 



class OmokViewSet(viewsets.ModelViewSet):
    queryset = Stone.objects.all()
    serializer_class = OmokSerializer



