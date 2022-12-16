import json

from django.http import JsonResponse
from rest_framework.decorators import api_view


from exrc.fashion.fashion_service import FashionService


@api_view(['GET', 'POST'])
def fashion(request):
    result = None
    if request.method == 'GET':
        print(f"######## Get test_num is {request.GET['test_num']} ########")
        result = FashionService().service_model(int(request.GET['test_num']))

    elif request.method == 'POST':
        data = json.loads(request.body)  # json to dict
        print(f"######## Post test_num is {data['test_num']} ########")
        result = FashionService().service_model(int(data['test_num']))

    return JsonResponse({'result': result})
