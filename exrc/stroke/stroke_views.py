from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from exrc.stroke.stroke_model import StrokeService


@api_view(['POST'])
@parser_classes([JSONParser])
def stroke(request):
    StrokeService().stroke_hook()
    print(f'Enter Stroke with {request}')
    return JsonResponse({'Response Test ': 'SUCCESS'})
