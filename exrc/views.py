from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from exrc.iris_model import IrisModel
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
    IrisModel().iris_hook()
    print(f'Enter Iris with {request}')
    return JsonResponse({'Response Test ': 'SUCCESS'})
