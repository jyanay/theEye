from datetime import datetime
from rest_framework.test import APIClient
from django.utils import timezone
from django.test import TestCase
from theEye.models import Event, Session
from theEye.views import PostEvent

'''
Model Tests
'''


class ModelsTestCase(TestCase):
    def setUp(self):
        session = Session.objects.create(session_id='e2085be5-9137-4e4e-80b5-f1ffddc25423')
        Event.objects.create(session_id=session,
                             category='Category',
                             name='Event',
                             data={'test': 'case'},
                             timestamp='2021-01-01 09:15:27.243860')

    def test_model_correct(self):
        test_session = Session.objects.get(id=1)
        test_event = Event.objects.get(name='Event')

        self.assertEqual(str(test_session.session_id), 'e2085be5-9137-4e4e-80b5-f1ffddc25423')
        self.assertEqual(str(test_event.session_id), 'e2085be5-9137-4e4e-80b5-f1ffddc25423')
        self.assertEqual(test_event.category, 'Category')
        self.assertEqual(test_event.name, 'Event')
        self.assertEqual(test_event.data, {'test': 'case'})
        self.assertEqual(test_event.timestamp, datetime.fromisoformat('2021-01-01 09:15:27.243860+00:00'))


'''
View Tests
'''

client = APIClient()


def PostEventTests(TestCase):
    def test_no_data(self):
        request = client.post('/post/create', {'data': ''}, format('json'))
        self.assertEqual(request, request.status_code == 400)

    '''
    And so on
    '''


'''

'''