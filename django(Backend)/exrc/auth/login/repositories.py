from django.http import JsonResponse
from rest_framework.response import Response

from exrc.auth.exrc_users.models import Users
from exrc.auth.exrc_users.serializers import UserSerializer


class UserRepository(object):

    def find_by_id(self, id):
        return Users.objects.all().filter(id=id).values()[0]

    def login(self, param):
        loginUser = Users.objects.get(user_email=param['user_email'])
        if loginUser.password == param['password']:
            dbUser = self.find_by_id(loginUser.id)
            serializer = UserSerializer(dbUser, many=False)
            return JsonResponse(data=serializer.data, safe=False)
            # dictionary 이외를 받을 경우, 두 번째 argument를 safe=False로 설정해야 한다.
        else:
            return JsonResponse({'result': 'WRONG PASSWORD'})

    def select_all(self):
        return Response(UserSerializer(Users.objects.all(), many=True).data)

    def get_all(self):
        return Response(UserSerializer(Users.objects.all(), many=True).data)


