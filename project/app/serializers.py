from rest_framework import serializers

class Studentserializers(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=40)
    city=serializers.CharField(max_length=40)
    roll=serializers.IntegerField()