import json
import logging
import datetime

from django.views import View
from django.http import JsonResponse

from .models import *

logger = logging.getLogger('django')

class CaseView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            name = data['name']
            code = data['code']

            test, flag = Case.objects.get_or_create(name = name, code = code)

            logger.info("{} {} {} 200".format(request.method, request.path, request.headers['User-Agent']))

            return JsonResponse({'Message' : 'Check', 'Result' : test.id}, status = 200)

        except KeyError:
            logger.warn("{} {} {} 400 : KeyError".format(request.method, request.path, request.headers['User-Agent']))
            return JsonResponse({'Message' : 'KeyError'}, status = 400)

    def get(self, request):
        data = Case.objects.all()
        if not data:
            logger.info("{} {} {} 200".format(request.method, request.path, request.headers['User-Agent']))

            return JsonResponse({'Message' : 'Empty Case data'}, status = 200)

        res = [ {
            'name' : case.name,
            'code' : case.code
        } for case in data ]

        logger.info("{} {} {} 200".format(request.method, request.path, request.headers['User-Agent']))

        return JsonResponse({'Message' : 'All Case data', 'Response' : res}, status = 200)
