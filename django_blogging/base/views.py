import json
import logging
import datetime

from django.views      import View
from django.http       import JsonResponse
from django.core.cache import cache

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

            if flag:
                data = Case.objects.all()
                temp_data = [ {
                    'name' : case.name,
                    'code' : case.code
                } for case in data ]
                cache.set('all_cases', temp_data)

            return JsonResponse({'Message' : 'Check', 'Result' : test.id}, status = 200)

        except KeyError:
            logger.warn("{} {} {} 400 : KeyError".format(request.method, request.path, request.headers['User-Agent']))
            return JsonResponse({'Message' : 'KeyError'}, status = 400)

    def get(self, request):
        data = Case.objects.all()
        if not data:
            logger.info("{} {} {} 200".format(request.method, request.path, request.headers['User-Agent']))

            return JsonResponse({'Message' : 'Empty Case data'}, status = 200)

        all_cases = cache.get('all_cases')
        if not all_cases:
            temp_data = [ {
                'name' : case.name,
                'code' : case.code
            } for case in data ]
            cache.set('all_cases', temp_data)
            all_cases = temp_data

        logger.info("{} {} {} 200".format(request.method, request.path, request.headers['User-Agent']))

        return JsonResponse({'Message' : 'All Case data', 'Response' : all_cases}, status = 200)

def SizeSearch(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        target_size = data['size']

        size_obj = Size.objects.get(name = target_size)
        if not size_obj:
            return JsonResponse({'Message' : 'INVALID_INPUT'}, status = 400)

        temp_data = SpecificProduct.objects.filter(size = size_obj)
        if not temp_data:
            return JsonResponse({'Message' : 'Empty selected size product'}, status = 200)

        result = [ { 'Product Name' : product.product.name } for product in temp_data ]

        return JsonResponse({'Message' : 'Size searching result', 'Result' : result}, status = 200)

def AllProduct(request):
    if request.method == 'GET':
        temp_data = SpecificProduct.objects.all()
        if not temp_data:
            return JsonResponse({'Message' : 'Empty specific product table'}, status = 200)

        result = [ product_info.id for product_info in temp_data ]

        return JsonResponse({'Message' : 'All specific product ID list', 'Result' : result}, status = 200)

def SelectRelatedPrac(request, product_id):
    if request.method == 'GET':
        target_id = product_id

        temp_data = SpecificProduct.objects.select_related('product', 'size').get(id = target_id)
        if not temp_data:
            return JsonResponse({'Message' : 'INVALID_SPECIFIC_PRODUCT_VALUE'}, status = 400)

        result = {
            'Product Name' : temp_data.product.name,
            'Product Size' : temp_data.size.name,
            'Product Weight' : temp_data.size.weight
        }

        return JsonResponse({'Message' : 'Selected product specific information', 'Result' : result}, status = 200)
