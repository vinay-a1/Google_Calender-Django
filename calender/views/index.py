
# Djano Imports
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Index/Home Page, Oauth2 Login
def HomeView(request):
    return render(request, 'home.html')

# Get ClientId for html
class ClientId(APIView):
    def get(self,request):
        return Response({
            "clientId":f"{settings.GOOGLE_OAUTH2_CLIENT_ID}"
            }, status=status.HTTP_200_OK)
