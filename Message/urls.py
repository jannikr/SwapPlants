from django.urls import path
from Message.views import messages, directs, send_direct

urlpatterns = [
    path('nachrichten/', messages, name='messages'),
    path('nachrichten/<username>', directs, name='directs'),
    path('send/', send_direct, name='send_direct'),
]
