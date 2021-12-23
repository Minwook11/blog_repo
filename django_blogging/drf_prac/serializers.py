from rest_framework import serializers
from .models import Practice, Nested, Student, Lecture, Enrolment

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

class WriteStudentSerializer(serializers.Serializer):
	name = serializers.CharField()
	age = serializers.IntegerField()
	grade = serializers.IntegerField()

	def create(self, validated_data):
		student, flag = Student.objects.get_or_create(**validated_data)
		return student

class ReadStudentSerializer(serializers.Serializer):
	class Meta:
		model = Student
		fields = {'__all__'}

class WriteLectureSerializer(serializers.Serializer):
	name = serializers.CharField()
	length = serializers.IntegerField()
	is_compulsory = serializers.BooleanField()

	def create(self, validated_data):
		lecture, flag = Lecture.objects.get_or_create(**validated_data)
		return lecture

class ReadLectureSerializer(serializers.Serializer):
	class Meta:
		model = Lecture
		fields = {'__all__'}

class WriteEnrolmentSerializer(serializers.Serializer):
	student = WriteStudentSerializer()
	lecture = WriteLectureSerializer()

	def create(self, validated_data):
		student_data = validated_data.pop('student')
		lecture_data = validated_data.pop('lecture')
		student_obj, f = Student.objects.get_or_create(**student_data)
		lecture_obj, f = Lecture.objects.get_or_create(**lecture_data)
		enrolment, flag = Enrolment.objects.get_or_create(student = student_obj, lecture = lecture_obj)
		return enrolment

class ReadEnrolmentSerializer(serializers.Serializer):
	class Meta:
		model = Enrolment
		fields = {'__all__'}
