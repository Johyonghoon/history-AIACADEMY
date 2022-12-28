from django.http import JsonResponse
from rest_framework.decorators import api_view

from exrc.webcrawler.naver_movie.services import ScrapService


@api_view(['GET'])
def api(request):
    result = ScrapService().naver_movie_review()
    print(f'### No.1 movie at Naver Movie is {result} ###')
    return JsonResponse({'result': result})
