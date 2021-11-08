from rest_framework import serializers
from theEye.models import Event, Session
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['category', 'name', 'data', 'timestamp']

    def validate_timestamp(self, value):
        """
        Checks if timestamp is in the future
        :param value: timestamp
        :return: Raises ValidationError if validation fails
        """
        if value > timezone.now():
            logger.error('POST Request with future timestamp')
            raise serializers.ValidationError("Time stamp is in the future.")

    def validate_category(self, value):
        """
        :param value: category value
        :return: Raises ValidationError if validation fails
        """
        pass

    def validate_name(self, value):
        """
        :param value: name value
        :return: Raises ValidationError if validation fails
        """
        pass

    def validate_data(self, value):
        """
        :param value: data value -- JSON
        :return: Raises ValidationError if validation fails
        """
        pass
