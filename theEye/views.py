
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from theEye.serializers import EventSerializer
from theEye.tasks import save_event
import logging

logger = logging.getLogger(__name__)


class PostEvent(APIView):
    """
    Receives a Post request of new Event
    Expecting JSON payload in the format:
        {
          "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
          "category": "page interaction",
          "name": "pageview",
          "data": {
            "host": "www.consumeraffairs.com",
            "path": "/",
          },
          "timestamp": "2021-01-01 09:15:27.243860"
        }
    """
    def get(self):
        pass

    def post(self, request):
        try:
            data = {
                'session_id': request.data.get('session_id'),
                'category': request.data.get('category'),
                'name': request.data.get('name'),
                'data': request.data.get('data'),
                'timestamp': request.data.get('timestamp')
            }
        except ValueError:
            logger.error('POST Request did not contain expected values')
            return Response('Invalid Format', status=status.HTTP_400_BAD_REQUEST)

        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            save_event.delay(data)
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






