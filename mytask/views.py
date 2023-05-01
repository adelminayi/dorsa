from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny


from .models import AddValues

# Create your views here.
class Adel(APIView):
    permission_classes=[AllowAny]

    def get (self, request, *args, **kwargs):
        # query = Secret.objects.filter(profile=5)
        # print(query)
        return HttpResponse({'condition': 'true'})