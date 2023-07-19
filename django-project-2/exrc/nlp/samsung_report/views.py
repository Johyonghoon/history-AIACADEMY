from django.http import JsonResponse
from rest_framework.decorators import api_view
from exrc.nlp.samsung_report.services import Controller


@api_view(['GET'])
def api(request):
    result = Controller().data_analysis()
    print(f'### No.1 movie at Naver Movie is {result} ###')
    return JsonResponse({'result': result})
