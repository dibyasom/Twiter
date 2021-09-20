from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status

from rest_framework.parsers import JSONParser

from tweet.models import Tweet
from tweet.serializers import TweetSerializer

# Create your views here.


@csrf_exempt
def tweets(request: HttpRequest) -> HttpResponse:
    '''
    List all tweets from DB.
    '''
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def tweet(request: HttpRequest, pk: int) -> HttpResponse:

    try:
        # Fetch the tweek.
        tweet = Tweet.objects.get(pk=pk)
    except Tweet.DoesNotExist:
        return HttpResponse(status=404)

    # Return Tweet details.
    if request.method == 'GET':
        # Serialize and return JSON res.
        serializer = TweetSerializer(tweet)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    # Delete tweet.
    if request.method == 'DELETE':
        tweet.delete()
        return HttpResponse(status=204)

    # Update/Edit tweet.
    if request.method == 'PUT':
        # Convert to native python datatype.
        data = JSONParser().parse(request)
        
        # Deserialize
        serializer = TweetSerializer(tweet, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    return HttpResponse(status=404)
