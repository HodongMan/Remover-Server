from rest_framework import serializers

from .models import Declare

class DeclareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Declare
        fields = (
            'pk',
            'user',
            'title',
            'description',
            'created'
        )