# drf request, response
from rest_framework import generics

from tweet.models import Tweet
from tweet.serializers import TweetSerializer

# DRF mixins
from rest_framework import generics


# All tweets.
class TweetList(generics.ListCreateAPIView):
    '''
        List all tweets or create new tweet.
    '''
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

# TODO: Implement PATCH to manipulate a single field of tweet.


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a tweet.
    """
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

# ####################################################### #
# MANUAL WAY, More control. w/o using generics or mixins. #
# ####################################################### #

# # All tweets.
# class TweetList(APIView):
#     '''
#         List all tweets or create new tweet.
#     '''

#     # List all tweets
#     def get(self, request: Request, format=None):
#         tweets = Tweet.objects.all()
#         serializer = TweetSerializer(tweets, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # Create new tweet.
#     def post(self, request: Request, format=None):
#         serializer = TweetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # TODO: Implement PATCH to manipulate a single field of tweet.

# class TweetDetail(APIView):
#     """
#     Retrieve, update or delete a tweet.
#     """

#     def get_tweet(self, pk):
#         try:
#             # Fetch the tweek.
#             return Tweet.objects.get(pk=pk)
#         except Tweet.DoesNotExist:
#             raise Response(status=status.HTTP_404_NOT_FOUND)

#     # Return Tweet details.
#     def get(self, request: Request, pk: int, format=None):
#         tweet = self.get_tweet(pk=pk)

#         # Serialize and return JSON res.
#         serializer = TweetSerializer(tweet)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # Update/Edit tweet.

#     def put(self, request: Request, pk: int, format=None):
#         tweet = self.get_tweet(pk=pk)

#         # Deserialize
#         serializer = TweetSerializer(tweet, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete tweet.
#     def delete(self, request: Request, pk: int, format=None):
#         tweet = self.get_tweet(pk=pk)

#         tweet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
