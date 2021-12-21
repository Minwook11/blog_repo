from rest_framework import serializers
from .models import Practice, Nested

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

class ReadNestedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Nested
		fields = ('date', 'nested_1')

class WriteNestedSerializer(serializers.Serializer):
	prac = WritePracticeSerializer()
	nested_1 = serializers.CharField()

	def create(self, validated_data):
		nested_data = validated_data.pop('nested_1')
		practice_data = validated_data.pop('prac')
		prac_obj = Practice.objects.create(**practice_data)
		return Nested.objects.create(prac = prac_obj, nested_1 = nested_data)
