from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from exrc.auth.exrc_users.services import UsersService


@api_view(['POST'])
@parser_classes([JSONParser])
def api(request):
    UsersService.create_acc_hook()
    print(f'### 더미 사용자 100명이 데이터베이스에 생성되었습니다.  ###')
    return JsonResponse({'result': 'Success'})

