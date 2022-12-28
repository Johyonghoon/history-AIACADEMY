from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from exrc.auth.exrc_users.services import UsersService


@api_view(['POST'])
@parser_classes([JSONParser])
def api(request):
    service = UsersService()
    service.create_acc_hook()
    print(f'### DB에 더미 사용자 100명을 생성했습니다. ###')
    return JsonResponse({'result': 'Success'})

def user_list(request):
    UsersService().get_accounts()
    return JsonResponse({'result': 'Success'})
