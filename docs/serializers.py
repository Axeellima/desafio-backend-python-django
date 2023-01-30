from rest_framework import serializers
import ipdb
from .models import Doc

class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = ["id", "type", "event_date", "cpf", "card", "hour", "owner", "store", "value"]
        read_only_fields = [ "type", "event_date","cpf", "card", "hour", "owner", "store", "value"]

class DocListSerializer(serializers.Serializer):
    data = DocSerializer(many=True, read_only=True)

    def create(self, validated_data):
        for line in validated_data["data"]:
            doc = Doc.objects.create(**line)
        return doc

    def save(self, **kwargs):
        return super().save(**kwargs)