from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import InvalidMethodThrottle

from .models import AddValues
from .serializers import GetAddSerializer, SumSerializer, all_adds, all_results

class Adel(APIView):
    permission_classes=[AllowAny]

    def get (self, request, *args,**kwargs):
        a = request.GET.get('a', None)
        # print(type(a))
        b = request.GET.get('b', None)
        # print(type(b))
        # print('+++++++++++++++++')
        # result = int(a)+int(b)
        # print(result)
        # values = {'avalue': self.request.query_params.get('a', None) , 'bvalue': self.request.query_params.get('b', None)}
        if a is None or b is None:
            return Response({'response':'Invalid params name!'}, status=status.HTTP_400_BAD_REQUEST)
        values = {'avalue': a , 'bvalue': b, 'sumvalue': int(a)+int(b)}
        serializer = GetAddSerializer(data=values)
        if serializer.is_valid():
            serializer.save()            
            return Response({'result': int(self.request.query_params.get('a')) + int(self.request.query_params.get('b')) }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class sumView(APIView):
    permission_classes=[AllowAny]
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        values = {'avalue': self.request.query_params.get('a') , 'bvalue': self.request.query_params.get('b')}

        serializer = SumSerializer(data = values)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': int(self.request.query_params.get('a')) + int(self.request.query_params.get('b')) }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class totalView(APIView):
    permission_classes= [IsAuthenticated]
    throttle_classes = [InvalidMethodThrottle]

    def get(self, request):
        queryset = AddValues.objects.all()
        serializer = all_adds(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class historyView(APIView):
    permission_classes= [IsAuthenticated]
    throttle_classes = [InvalidMethodThrottle]

    def get(self, request):
        queryset = AddValues.objects.all()
        serializer = all_results(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
