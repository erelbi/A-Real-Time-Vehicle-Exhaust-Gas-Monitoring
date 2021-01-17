from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views import View

from rest_framework.views import APIView

from sensors.models import SensorA
from sensors.serializers import SensorASerilazer
from rest_framework import viewsets,mixins,generics
from rest_framework.response import Response
from rest_framework import status


class SensorA(APIView):
    queryset = SensorA.objects.all()
    serializer_cla = SensorASerilazer
    def post(self,request, *args, **kwargs):
        serializer = SensorASerilazer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Home(View):
    def get(self, request, *args, **kwargs):
        response = TemplateResponse(request, 'index.html')
        return response

