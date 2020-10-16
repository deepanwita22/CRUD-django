from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import General_detail
from django.http import HttpResponse
from django.core.exceptions import MultipleObjectsReturned
from .serializers import General_detailSerializer
import json
from django.http import JsonResponse


class General_detailList(APIView):

    def get(self,request):
        gen_det = General_detail.objects.all()
        serializer = General_detailSerializer(gen_det,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        
        serializer=General_detailSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)     

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


class GetbyID_detailList(APIView):
    
    def get(self,request,pk):
        det = General_detail.objects.get(pk=pk)
        serializer = General_detailSerializer(det)
        return Response(serializer.data)


class Update_detailList(APIView):

    def put(self,request,pk):
        try:
            det = General_detail.objects.get(pk=pk)
        except General_detail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer=General_detailSerializer(det,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Delete_detailList(APIView):

    def delete(self,request,pk):
        try:
            det = General_detail.objects.get(pk=pk)
        except General_detail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        det.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

