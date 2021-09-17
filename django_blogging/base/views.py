import json
import logging
import datetime

from django.views import View
from django.http import JsonResponse

from .models import *

logger = logging.getLogger('django')

class CaseView(View):
    def post(self, request):

        data = json.loads(request.body)
        name = data['name']
        code = data['code']

        test, flag = Case.objects.get_or_create(name = name, code = code)

        logger.info("{} {} {} 200".format(request.method, request.path, request.headers['User-Agent']))

        return JsonResponse({'Message' : 'Check', 'Result' : test.id}, status = 200)
