from rest_framework import serializers
from tweet.models import Tweet, LANGUAGE_CHOICES, STYLE_CHOICES


class TweetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        fields = ['id', 'username', 'content', 'language', 'style', 'linenos']

    def create(self, validated_data):
        """
        Create and return a new `Tweet` instance, given the validated data.
        """
        return Tweet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Tweet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.content = validated_data.get('content', instance.content)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
        
# from tweet.models import Tweet
# from tweet.serializers import TweetSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser