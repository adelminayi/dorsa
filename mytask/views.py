from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from .throttles import CustomRateThrottle
from .models import AddValues
from .serializers import SumSerializer, all_adds, all_results


class sumView(APIView):
    permission_classes=[AllowAny]
    throttle_classes = [AnonRateThrottle]

    def get(self, request):
        a = self.request.query_params.get('a')
        b = self.request.query_params.get('b')
        if a is None or b is None:
            return Response({'response':'Invalid params name!'}, status=status.HTTP_400_BAD_REQUEST)
        values = {'avalue': a , 'bvalue': b}
        serializer = SumSerializer(data = values)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': int(self.request.query_params.get('a')) + int(self.request.query_params.get('b')) }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class totalView(APIView):
    permission_classes= [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, CustomRateThrottle]

    def get(self, request):
        queryset = AddValues.objects.all()
        serializer = all_adds(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class historyView(APIView):
    permission_classes= [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, CustomRateThrottle]

    def get(self, request):
        queryset = AddValues.objects.all()
        serializer = all_results(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
