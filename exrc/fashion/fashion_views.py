import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from exrc.fashion.fashion_service import FashionService


@api_view(['POST', 'GET'])
def fashion(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # json to dict
        print(f"######## Post test_num is {data['test_num']} ########")
        return JsonResponse({'result': FashionService().service_model(int(data['test_num']))})

    elif request.method == 'GET':
        print(f"######## Get test_num is {request.GET['test_num']} ########")
        return JsonResponse(
            {'result': FashionService().service_model(int(request.GET['test_num']))})

    else:
        print(f"######## test_num is None ########")

    """
    # 초기 버전
    if request.method == 'POST':
        data = request.data
        test_num = tf.constant(int(data['test_num']))
        result = FashionService().service_model([test_num])
        return JsonResponse({'result': result})
    # 신 버전
    if request.method == 'POST':
        data = json.loads(request.body)  # json to dict
        print(f"######## test_num is {data['test_num']} ########")
        return JsonResponse({'result': FashionService().service_model(int(data['test_num']))})
    """
