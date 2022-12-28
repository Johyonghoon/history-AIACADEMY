import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

from exrc.nlp.imdb.services import NaverMovieService


@api_view(['POST'])
def api(request):
    review = json.loads(request.body)  # json to dict
    print(f"######## Post review is {review} ########")
    result = NaverMovieService().Naver_movie_hook(review['inputs'])
    return JsonResponse({'result': str(result)})
