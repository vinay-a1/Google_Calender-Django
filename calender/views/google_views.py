


from django.http import HttpResponseRedirect


# DRF Imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Calender API & Utils
from ..calender import calenderAPI
from ..utils import get_access_token_google


class GoogleCalendarInitView(APIView):
    
    def get(self,request, *args, **kwrags):
        
        access_token = get_access_token_google(code=request.GET.get('code'),
                                               redirect_uri='http://localhost:8000/rest/v1/calender/init')
        
        print(access_token)
        return HttpResponseRedirect(f'http://localhost:8000/rest/v1/calender/redirect?token={access_token}')
    

class GoogleCalendarRedirectView(APIView):
    
    def get(self,request, *args,**kwargs):
        access_token = request.GET.get('token')
        if not access_token:
            return Response({
                "error":"Acess token could not be found, Please try again!"
            })
            
        events = calenderAPI(access_token)
        
        return Response(events, status=status.HTTP_200_OK)
            
        