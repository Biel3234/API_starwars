from rest_framework import serializers

class NavesSerializer(serializers.Serializer):
    name = serializers.CharField()
    model = serializers.CharField()
    manufacturer = serializers.CharField()
    cost_in_credits = serializers.CharField()
    max_atmosphering_speed = serializers.CharField()
    crew = serializers.CharField()
    passengers = serializers.CharField()
    cargo_capacity = serializers.CharField()
    pilots = serializers.ListField(child = serializers.CharField())