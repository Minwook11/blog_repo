from rest_framework import viewsets
from .serializers import PracticeSerializer
from .models import Practice

class PracticeViewSet(viewsets.ModelViewSet):
	queryset = Practice.objects.all()
	serializer_class = PracticeSerializer

