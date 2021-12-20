from rest_framework import serializers
from .models import Practice

class PracticeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Practice
		fields = ('__all__')

class WritePracticeSerializer(serializers.Serializer):
	attr_1 = serializers.IntegerField()
	attr_2 = serializers.IntegerField()
	attr_3 = serializers.IntegerField()

	def create(self, validated_data):
		return Practice.objects.create(**validated_data)
