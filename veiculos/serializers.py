from rest_framework import serializers

class VeiculosSerializer(serializers.Serializer):
    name = serializers.CharField()
    model = serializers.CharField()
    manufacturer = serializers.CharField()
    cost_in_credits = serializers.CharField()
    max_atmosphering_speed = serializers.CharField()
    crew = serializers.CharField()
    passengers = serializers.CharField()
    cargo_capacity = serializers.CharField()
    consumables = serializers.CharField()
    vehicle_class = serializers.CharField()
    pilots = serializers.ListField(child=serializers.URLField())
    films = serializers.ListField(child=serializers.URLField())
