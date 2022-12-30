from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from exrc.auth.login.repositories import UserRepository
from exrc.auth.login.serializers import UserSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@parser_classes([JSONParser])
def users(request):
    if request.method == "GET":
        return UserRepository().find_by_id(request.data)
    elif request.method == "POST":
        return UserSerializer().create(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        return UserSerializer().update()
    elif request.method == "DELETE":
        return UserSerializer().delete()


@api_view(['GET'])
@parser_classes([JSONParser])
def user_list(request): return UserRepository().get_all()


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request): return UserRepository().login(request.data)
