from celery import shared_task
from theEye.models import Event, Session


@shared_task
def save_event(data):
    """
    Creates database entry in background
    :param dict from POST request
    creates or gets Session object, creates Event
    Saves to DB
    """
    session_id = data.pop('session_id')
    session = Session.objects.get_or_create(session_id=session_id)
    session[0].save()
    event = Event.objects.create(session_id=session[0], **data)
    event.save()
