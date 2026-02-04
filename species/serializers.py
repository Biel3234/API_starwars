from rest_framework import serializers

class SpeciesSerializer(serializers.Serializer):
    name = serializers.CharField()
    classification = serializers.CharField()
    designation = serializers.CharField()
    average_height = serializers.CharField()
    average_lifespan = serializers.CharField()
    hair_colors = serializers.CharField()
    skin_colors = serializers.CharField()
    eye_colors = serializers.CharField()
    language = serializers.CharField()
    people = serializers.ListField(child=serializers.URLField())
    films = serializers.ListField(child=serializers.URLField())
