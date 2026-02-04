from rest_framework import serializers

class PersonagensSerializer(serializers.Serializer):
    name = serializers.CharField()
    gender = serializers.CharField()
    height = serializers.CharField()
    hair_color = serializers.CharField()
    eye_color = serializers.CharField()
    mass = serializers.CharField()
    species = serializers.ListField(child=serializers.CharField())
    starships = serializers.ListField(child=serializers.CharField())
    vehicles = serializers.ListField(child=serializers.CharField())