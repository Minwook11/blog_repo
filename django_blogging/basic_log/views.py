import json

from django.views import View
from django.http import JsonResponse

from .models import *

class CaseView(View):
    def post(self, request):

        data = json.loads(request.body)
        name = data['name']
        code = data['code']

        test, flag = Case.objects.get_or_create(name = name, code = code)

        return JsonResponse({'Message' : 'Check', 'Result' : test.id}, status = 200)
