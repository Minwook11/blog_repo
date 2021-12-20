from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PracticeSerializer, WritePracticeSerializer
from .models import Practice

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

