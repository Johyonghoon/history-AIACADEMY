from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from exrc.iris_model import IrisModel
from exrc.iris_service import IrisService
from exrc.stroke import StrokeService


@api_view(['GET'])
@parser_classes([JSONParser])
def stroke(request):
    StrokeService().stroke_hook()
    print(f'Enter Stroke with {request}')
    return JsonResponse({'Response Test ': 'SUCCESS'})


@api_view(['POST'])
@parser_classes([JSONParser])
def iris(request):
    iris_info = request.data
    sepal_width = tf.constant(float(iris_info['sepal_width']))
    sepal_length = tf.constant(float(iris_info['sepal_length']))
    petal_width = tf.constant(float(iris_info['petal_width']))
    petal_length = tf.constant(float(iris_info['petal_length']))
    print(f"꽃받침의 너비: {sepal_width}\n"
          f"꽃받침의 길이: {sepal_length}\n"
          f"꽃잎의 너비: {petal_width}\n"
          f"꽃잎의 길이: {petal_length}")
    iris_species = IrisService().service_model([sepal_width, sepal_length, petal_width, petal_length])
    print(f'찾는 품종: {iris_species}')
    if iris_species == 0:
        resp = 'setosa / 부채붓꽃'
        print(resp)
    elif iris_species == 1:
        resp = 'versicolor / 버시칼라'
        print(resp)
    elif iris_species == 2:
        resp = 'virginica / 버지니카'
        print(resp)
    return JsonResponse({'result': resp})


