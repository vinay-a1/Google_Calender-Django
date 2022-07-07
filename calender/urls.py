from django.urls import path
from .views.google_views import (
    GoogleCalendarInitView, GoogleCalendarRedirectView
)
from .views.index import (
    ClientId, HomeView
)

home_urls = [
    path('clientId', ClientId.as_view()),
    path('', HomeView),
]


google_urls = [
    path('rest/v1/calender/init', GoogleCalendarInitView.as_view()),
    path('rest/v1/calender/redirect',GoogleCalendarRedirectView.as_view())
    
]

urlpatterns =home_urls+google_urls
