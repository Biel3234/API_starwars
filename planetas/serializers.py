from rest_framework import serializers

class PlanetaSerializer(serializers.Serializer):
    name = serializers.CharField()
    climate = serializers.CharField()
    terrain = serializers.CharField()
    population = serializers.CharField()
    diameter = serializers.CharField()
    gravity = serializers.CharField()
    rotation_period = serializers.CharField()
    orbital_period = serializers.CharField()
    surface_water = serializers.CharField()
    residents = serializers.ListField(
        child=serializers.URLField()
    )
    films = serializers.ListField(
        child=serializers.URLField()
    )