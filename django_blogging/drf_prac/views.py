from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PracticeSerializer, WritePracticeSerializer, WriteNestedSerializer, ReadNestedSerializer, WriteEnrolmentSerializer, WriteStudentSerializer
from .models import Practice, Nested

@api_view(['POST'])
def EnrolmentView(request):
	if request.method == 'POST':
		serializer_class = WriteEnrolmentSerializer(data = request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status = status.HTTP_200_OK)
		else:
			return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST',  'GET'])
def StudentView(request):
	if request.method == 'POST':
		serializer_class = WriteStudentSerializer(data = request.data)
		if serializer_class.is_valid():
			print('check1')
			serializer_class.save()
			return Response(serializer_class.data, status = status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def NestedView(request):
	if request.method == 'POST':
		serializer_class = WriteNestedSerializer(data = request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status = status.HTTP_200_OK)

		else:
			return Response(status = status.HTTP_400_BAD_REQUEST)

	elif request.method == 'GET':
		all_data = Nested.objects.all()
		serializer_class = ReadNestedSerializer(all_data, many = True).data

		return Response(serializer_class)

@api_view(['GET', 'POST'])
def PracticeView(request):
	if request.method == 'GET':
		all_data = Practice.objects.all()
		serializer_class = PracticeSerializer(all_data, many = True).data
		
		return Response(serializer_class)

	elif request.method == 'POST':
		serializer_class = WritePracticeSerializer(data = request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(data = serializer_class.data, status = status.HTTP_200_OK)
		else:
			return Response(status = status.HTTP_400_BAD_REQUEST)

class PracticeViewSet(viewsets.ModelViewSet):
	queryset = Practice.objects.all()
	serializer_class = PracticeSerializer

