from __future__ import print_function

import datetime

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.conf import settings

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def calenderAPI(access_token):
  
    creds = None
  
    if access_token:
        creds = Credentials(
            token=access_token,
            token_uri='https://www.googleapis.com/oauth2/v4/token',
            client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
            client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            scopes=SCOPES
        )
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired:
            return "Error, Token Expired, Please Try again!"
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            data = {}
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            data.update(start,event['summary'])
        return data

    except HttpError as error:
        return f"Error Occurred: {error}" 