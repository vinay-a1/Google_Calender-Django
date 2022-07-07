
# Django Settings Import
from django.conf import settings

# DRF Import
from rest_framework.validators import ValidationError

# Additional Imports
import requests
from typing import Dict, Any

GOOGLE_AUTH_URL='https://www.googleapis.com/oauth2/v4/token'
GOOGLE_USER_INFO_URL='https://www.googleapis.com/oauth2/v1/userinfo'

def get_access_token_google(*,code:str, redirect_uri: str) -> str:
    data = {
        'code':code,
        'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
        'client_secret': settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    response = requests.post(GOOGLE_AUTH_URL, data=data)
    if not response.ok:
        raise ValidationError("Failed to obtain access token from Google.")
    access_token = response.json()['access_token']
    
    return access_token

def google_get_user_info(*, access_token: str) -> Dict[str, Any]:
    response = requests.get(
        GOOGLE_USER_INFO_URL,
        params={'access_token': access_token}
    )
    if not response.ok:
        raise ValidationError('Failed to obtain user info from Google.')
    return response.json()