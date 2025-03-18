from rest_framework import serializers
from modelTrial.models import Firstname

class FirstnameSerializer (serializers.ModelSerializer):
    class Meta:
        model = Firstname
        fields = '__all__'