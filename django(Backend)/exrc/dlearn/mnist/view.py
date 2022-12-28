import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

from exrc.dlearn.mnist.service import MnistService


@api_view(['GET', 'POST'])
def api(request):
    result = None
    if request.method == 'GET':  # 'POST' 방식도 JSON을 처리하는 방식이 아닌 입력된 값을 바로 사용 가능
        print(f"######## Get test_num is {request.GET['test_num']} ########")
        result = MnistService().service_model(int(request.GET['test_num']))

    elif request.method == 'POST':
        test_num = json.loads(request.body)  # json to dict
        print(f"######## Post test_num is {test_num} ########")
        result = MnistService().service_model(int(test_num))

        """
        print(f"######## Post test_num is {request.POST['test_num']} ########")
        result = FashionService().service_model(int(request.POST['test_num']))
        """

    return JsonResponse({'result': result})
