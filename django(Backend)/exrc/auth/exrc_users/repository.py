from rest_framework.response import Response

from blog.views.models import View
from exrc.auth.exrc_users.serializers import UserSerializer


class ViewRepository(object):

    def __init__(self):
        print(" CommentsRepository 객체 생성 ")

    def get_all(self):
        return Response(UserSerializer(View.objects.all(), many=True).data)

    def get_by_id(self):
        return Response(UserSerializer(View.objects.all(), many=True).data)
